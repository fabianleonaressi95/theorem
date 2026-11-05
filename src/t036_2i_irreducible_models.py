"""Construct exact irreducible matrix models of 2I inside symmetric powers.

Uses T034 exact characters and the T035 exact 600-cell quaternion group.
Each irrep is isolated at its first Molien degree with multiplicity one.
The resulting invariant subspace has dimension d_rho and carries explicit
matrices for all 120 group elements over Q(sqrt(5), i).
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp

from src.t032_2i_molien import IRREP_DIMENSIONS, molien_coefficients
from src.t034_exact_2i_character_table import reconstruct_character_table
from audits.t035_exact_binary_icosahedral_model import (
    elements_2i, CLASS_SCALARS, expr, rho2
)

X, Y = sp.symbols("X Y")


def class_indices(group):
    return [CLASS_SCALARS.index(q[0]) for q in group]


def symmetric_power_matrix(M: sp.Matrix, degree: int) -> sp.Matrix:
    """Matrix of f(v) -> f(M^{-1}v) in X^(m-k)Y^k basis."""
    if degree < 0:
        raise ValueError("degree must be nonnegative")
    N = sp.simplify(M.inv())
    a,b,c,d = N[0,0],N[0,1],N[1,0],N[1,1]
    columns=[]
    for k in range(degree+1):
        polynomial=sp.expand((a*X+b*Y)**(degree-k)*(c*X+d*Y)**k)
        poly=sp.Poly(polynomial,X,Y)
        columns.append([sp.simplify(poly.coeff_monomial(X**(degree-r)*Y**r))
                        for r in range(degree+1)])
    return sp.Matrix(degree+1,degree+1,lambda r,k: columns[k][r])


def first_multiplicity_one_degrees(max_degree=40):
    from src.t032_2i_molien import IRREP_NUMERATORS
    result={}
    for label in IRREP_DIMENSIONS:
        candidates=[m for m in range(max_degree+1)
                    if molien_coefficients(label,m)[m]==1]
        if not candidates:
            raise ArithmeticError(f"No multiplicity-one occurrence for {label}")
        result[label]=candidates[0]
    return result


def exact_matrix_model(label: str, group, chars, degree: int):
    d=IRREP_DIMENSIONS[label]
    class_id=class_indices(group)
    chi=chars[label]
    ambient=degree+1
    P=sp.zeros(ambient)
    sym_cache=[]
    for q,j in zip(group,class_id):
        S=symmetric_power_matrix(rho2(q),degree)
        sym_cache.append(S)
        P += sp.conjugate(chi[j])*S
    P=sp.simplify(sp.Rational(d,120)*P)
    if sp.simplify(P*P-P)!=sp.zeros(ambient):
        raise AssertionError(f"central projector is not idempotent for {label}")
    basis=P.columnspace()
    if len(basis)!=d:
        raise AssertionError(f"projector rank for {label}: {len(basis)} != {d}")
    B=sp.Matrix.hstack(*basis)
    pivot_rows=tuple(B.T.rref()[1])
    if len(pivot_rows)!=d:
        raise AssertionError(f"could not select basis rows for {label}")
    Bp=B[list(pivot_rows),:]
    if Bp.det()==0:
        raise AssertionError(f"singular pivot minor for {label}")
    Bpinv=Bp.inv()
    matrices=[]
    for S in sym_cache:
        SB=S*B
        R=sp.simplify(Bpinv*SB[list(pivot_rows),:])
        if sp.simplify(SB-B*R)!=sp.zeros(ambient,d):
            raise AssertionError(f"invariant subspace failure for {label}")
        matrices.append(R)
    # The monomial basis of Sym^m(C^2) has invariant Gram diag(1/binomial(m,k)).
    W=sp.diag(*[sp.Rational(1,sp.binomial(degree,k))
                for k in range(degree+1)])
    gram=sp.simplify(B.conjugate().T*W*B)
    if gram.det()==0:
        raise AssertionError(f"induced Gram matrix singular for {label}")
    for R in matrices:
        if sp.simplify(R.conjugate().T*gram*R-gram)!=sp.zeros(d):
            raise AssertionError(f"invariant Hermitian form failure for {label}")
    return {
        "degree":degree,
        "dimension":d,
        "ambient_dimension":ambient,
        "projector_rank":len(basis),
        "basis":B,
        "gram":gram,
        "matrices":matrices,
        "pivot_rows":pivot_rows,
    }


def build_all_models():
    group=elements_2i()
    chars,_=reconstruct_character_table()
    degrees=first_multiplicity_one_degrees()
    models={}
    for label in IRREP_DIMENSIONS:
        models[label]=exact_matrix_model(label,group,chars,degrees[label])
    return group,chars,degrees,models


def verify_models(group, chars, degrees, models):
    labels=tuple(IRREP_DIMENSIONS)
    checks=0
    for label in labels:
        model=models[label]
        d=IRREP_DIMENSIONS[label]
        if model["projector_rank"]!=d: raise AssertionError("rank mismatch")
        if len(model["matrices"])!=120: raise AssertionError("missing group matrices")
        # Character recovery, all nine classes, by exact traces.
        trace_by_class={}
        for j in range(9):
            indices=[i for i,q in enumerate(group) if CLASS_SCALARS.index(q[0])==j]
            if not indices: raise AssertionError(f"empty class {j}")
            traces={sp.simplify(sp.trace(model["matrices"][i])) for i in indices}
            if len(traces)!=1: raise AssertionError("trace is not class-constant")
            value=traces.pop()
            if sp.simplify(value-chars[label][j])!=0:
                raise AssertionError(f"character mismatch {label}, class {j}")
            trace_by_class[j]=value
            checks+=1
        # Every matrix preserves the induced positive Hermitian form.
        G=model["gram"]
        for R in model["matrices"]:
            if sp.simplify(R.conjugate().T*G*R-G)!=sp.zeros(d):
                raise AssertionError(f"unitarity in invariant metric failed: {label}")
            checks+=1
    if sum(IRREP_DIMENSIONS[x]**2 for x in labels)!=120:
        raise AssertionError("sum of squares is not 120")
    return {"passed":True,"irreducibles":len(labels),
            "matrix_models":sum(len(models[x]["matrices"]) for x in labels),
            "character_values_recovered":checks-120*sum(IRREP_DIMENSIONS.values()),
            "invariant_metric_checks":120*sum(IRREP_DIMENSIONS.values()),
            "sum_dimension_squares":120,
            "first_multiplicity_one_degrees":degrees}


def json_payload(group,degrees,models,report):
    def mat(M): return [[sp.sstr(sp.simplify(M[i,j])) for j in range(M.cols)]
                        for i in range(M.rows)]
    elements=[]
    for q in group:
        elements.append([[str(x[0]),str(x[1])] for x in q])
    irreps={}
    for label,m in models.items():
        irreps[label]={
          "degree":m["degree"],"dimension":m["dimension"],
          "ambient_dimension":m["ambient_dimension"],
          "basis":mat(m["basis"]),"invariant_gram":mat(m["gram"]),
          "matrices_by_group_index":[mat(R) for R in m["matrices"]],
          "pivot_rows":list(m["pivot_rows"])
        }
    return {"group":"2I","order":120,"coefficient_field":"Q(sqrt(5), i)",
            "element_coordinates_Q_phi":elements,"irreps":irreps,
            "first_multiplicity_one_degrees":degrees,"verification":report}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",default="data/t036_2i_irreducible_models_exact.json")
    args=parser.parse_args()
    group,chars,degrees,models=build_all_models()
    report=verify_models(group,chars,degrees,models)
    payload=json_payload(group,degrees,models,report)
    path=Path(args.output); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()

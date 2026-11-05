"""Exact 2I-isotypic and multiplicity decomposition of Sym^m(C^2)."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp
from src.t032_2i_molien import IRREP_DIMENSIONS, molien_coefficients
from src.t034_exact_2i_character_table import reconstruct_character_table
from src.t036_2i_irreducible_models import build_all_models, symmetric_power_matrix
from audits.t035_exact_binary_icosahedral_model import elements_2i, CLASS_SCALARS, rho2

def class_indices(group):
    return tuple(CLASS_SCALARS.index(q[0]) for q in group)

def ambient_matrices(group, degree):
    return tuple(symmetric_power_matrix(rho2(q), degree) for q in group)

def intertwiner_basis(ambient, irrep_matrices, d):
    n=ambient[0].rows; In=sp.eye(n); Id=sp.eye(d); blocks=[]
    for U,R in zip(ambient,irrep_matrices):
        blocks.append(sp.kronecker_product(Id,U)-sp.kronecker_product(R.T,In))
    system=sp.Matrix.vstack(*blocks); vectors=system.nullspace(); maps=[]
    for v in vectors:
        X=sp.zeros(n,d)
        for col in range(d):
            for row in range(n): X[row,col]=v[col*n+row]
        maps.append(X)
    return tuple(maps),system.rows,system.cols

def decompose_degree(degree,group,chars,models):
    if degree<0: raise ValueError("degree must be nonnegative")
    U=ambient_matrices(group,degree); n=degree+1
    W=sp.diag(*[sp.Rational(1,sp.binomial(degree,k)) for k in range(n)])
    class_id=class_indices(group); result={}; all_images=[]; total=0
    for label,d in IRREP_DIMENSIONS.items():
        expected=molien_coefficients(label,degree)[degree]
        R=models[label]["matrices"]
        maps,equations,unknowns=intertwiner_basis(U,R,d)
        if len(maps)!=expected:
            raise AssertionError(f"Hom multiplicity {label}, m={degree}: {len(maps)} != {expected}")
        if expected:
            P=sp.zeros(n)
            for Ug,j in zip(U,class_id): P+=sp.conjugate(chars[label][j])*Ug
            P=sp.simplify(sp.Rational(d,120)*P)
            if sp.simplify(P*P-P)!=sp.zeros(n): raise AssertionError(f"projector idempotence: {label}")
            if P.rank()!=d*expected: raise AssertionError(f"projector rank: {label}")
            image_block=sp.Matrix.hstack(*maps)
            if image_block.rank()!=d*expected: raise AssertionError(f"dependent Hom images: {label}")
            for X in maps:
                for Ug,Rg in zip(U,R):
                    if sp.simplify(Ug*X-X*Rg)!=sp.zeros(n,d): raise AssertionError(f"intertwining: {label}")
                induced=sp.simplify(X.conjugate().T*W*X); G=models[label]["gram"]
                scalar=sp.simplify(sp.trace(G.inv()*induced)/d)
                if scalar==0 or sp.simplify(induced-scalar*G)!=sp.zeros(d):
                    raise AssertionError(f"Schur metric proportionality: {label}")
            all_images.extend(maps)
        result[label]={"dimension":d,"Molien_multiplicity":expected,
          "Hom_dimension":len(maps),"isotypic_dimension":d*expected,
          "central_projector_rank":d*expected if expected else 0,
          "intertwiner_equations":equations,"intertwiner_unknowns":unknowns,
          "multiplicity_basis":maps}
        total+=d*expected
    if total!=n: raise AssertionError(f"dimension decomposition {total} != {n}")
    if all_images and sp.Matrix.hstack(*all_images).rank()!=n:
        raise AssertionError("isotypic images do not span Sym^m")
    return result

def run(max_degree=8):
    group=elements_2i(); chars,_=reconstruct_character_table()
    _,_,_,models=build_all_models(); decompositions={}
    for m in range(max_degree+1):
        dec=decompose_degree(m,group,chars,models)
        decompositions[str(m)]={label:{k:v for k,v in entry.items() if k!="multiplicity_basis"}
                                for label,entry in dec.items()}
    return {"passed":True,"group_order":120,"degrees_checked":list(range(max_degree+1)),
      "degree_count":max_degree+1,"decompositions":decompositions,
      "scope":"Exact finite-degree Sym^m(C^2) decomposition; geometric Rumin differential restrictions remain a separate step."}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--max-degree",type=int,default=8)
    p.add_argument("--output",default="data/t037_rumin_harmonic_multiplicities.json"); a=p.parse_args()
    report=run(a.max_degree); path=Path(a.output); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k!="decompositions"},indent=2))
if __name__=="__main__": main()

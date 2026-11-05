"""T034 -- explicit exact representations of the binary icosahedral group 2I.

Everything here is exact arithmetic in K = Q(sqrt5)[i] using only
``fractions.Fraction``.  No floating point is used in any identity, and there
is no dependency on sympy or on the rgs-qlg-quaternion-bridge repository.

Conventions (inherited from T031/T033):
  * quaternions are scalar-first (w, x, y, z) with the Hamilton product;
  * 2I acts on S^3 = SU(2) by left multiplication q -> g q;
  * the left representation property is U(gh) = U(g) U(h);
  * matrix units: E_ij = (d/120) sum_g rho(g^{-1})_{ji} U(g), which equals the
    T033 formula (d/120) sum_g conj(rho(g)_{ij}) U(g) whenever rho is unitary.
    The inverse form is used because it is valid in *any* basis (the monomial
    bases of Sym^k below are unitary only for a diagonal weighted form).

Class order and fundamental character follow
bibliography/spin-geometry-quaternionic/RUMIN_2I_N1_CHARACTER_AUDIT.py
(as quoted in the existing T034 character-table note).
"""
from __future__ import annotations

import argparse
import itertools
import json
import random
from dataclasses import dataclass
from fractions import Fraction
from math import comb
from pathlib import Path

from src.t032_2i_molien import IRREP_DIMENSIONS, IRREP_NUMERATORS, molien_coefficients

ORDER = 120
LABELS = ("1", "2", "2'", "3", "3'", "4", "4'", "5", "6")
CLASS_SIZES = (1, 1, 20, 30, 12, 12, 20, 12, 12)
CLASS_ORDERS = (1, 2, 3, 4, 5, 5, 6, 10, 10)


# --------------------------------------------------------------------------
# Exact field K = Q(sqrt5)[i]:  a + b*sqrt5 + (c + d*sqrt5)*i
# --------------------------------------------------------------------------
class Num:
    __slots__ = ("a", "b", "c", "d")

    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = Fraction(a)
        self.b = Fraction(b)
        self.c = Fraction(c)
        self.d = Fraction(d)

    @staticmethod
    def of(x):
        return x if isinstance(x, Num) else Num(x)

    def __add__(self, o):
        o = Num.of(o)
        return Num(self.a + o.a, self.b + o.b, self.c + o.c, self.d + o.d)

    __radd__ = __add__

    def __neg__(self):
        return Num(-self.a, -self.b, -self.c, -self.d)

    def __sub__(self, o):
        o = Num.of(o)
        return Num(self.a - o.a, self.b - o.b, self.c - o.c, self.d - o.d)

    def __rsub__(self, o):
        return Num.of(o) - self

    def __mul__(self, o):
        o = Num.of(o)
        a1, b1, c1, d1 = self.a, self.b, self.c, self.d
        a2, b2, c2, d2 = o.a, o.b, o.c, o.d
        # real part R = R1 R2 - I1 I2, imaginary part I = R1 I2 + I1 R2,
        # each product taken in Q(sqrt5): (p+q s)(r+u s) = (pr+5qu) + (pu+qr) s
        ra = a1 * a2 + 5 * b1 * b2 - (c1 * c2 + 5 * d1 * d2)
        rb = a1 * b2 + b1 * a2 - (c1 * d2 + d1 * c2)
        ia = a1 * c2 + 5 * b1 * d2 + c1 * a2 + 5 * d1 * b2
        ib = a1 * d2 + b1 * c2 + c1 * b2 + d1 * a2
        return Num(ra, rb, ia, ib)

    __rmul__ = __mul__

    def scale(self, f):
        f = Fraction(f)
        return Num(self.a * f, self.b * f, self.c * f, self.d * f)

    def cconj(self):
        """complex conjugation (i -> -i), fixing sqrt5"""
        return Num(self.a, self.b, -self.c, -self.d)

    def gal(self):
        """Galois automorphism sqrt5 -> -sqrt5, fixing i"""
        return Num(self.a, -self.b, self.c, -self.d)

    def is_zero(self):
        return self.a == 0 and self.b == 0 and self.c == 0 and self.d == 0

    def is_real(self):
        return self.c == 0 and self.d == 0

    def key(self):
        return (self.a, self.b, self.c, self.d)

    def __eq__(self, o):
        if not isinstance(o, (Num, int, Fraction)):
            return NotImplemented
        o = Num.of(o)
        return self.key() == o.key()

    def __hash__(self):
        return hash(self.key())

    def encode(self):
        """machine-readable: [a,b,c,d] strings meaning a+b*sqrt5+(c+d*sqrt5)*i"""
        return [str(self.a), str(self.b), str(self.c), str(self.d)]

    def __repr__(self):
        parts = []
        if self.a != 0 or (self.b == 0 and self.c == 0 and self.d == 0):
            parts.append(str(self.a))
        if self.b != 0:
            parts.append(f"({self.b})*sqrt5")
        if self.c != 0:
            parts.append(f"({self.c})*i")
        if self.d != 0:
            parts.append(f"({self.d})*sqrt5*i")
        return "+".join(parts)


ZERO = Num(0)
ONE = Num(1)
I_UNIT = Num(0, 0, 1, 0)
SQRT5 = Num(0, 1)
PHI = Num(Fraction(1, 2), Fraction(1, 2))          # (1+sqrt5)/2
PHI_INV = PHI - 1                                   # (sqrt5-1)/2

FUNDAMENTAL_CHARACTER = (
    Num(2), Num(-2), Num(-1), Num(0),
    PHI - 1, -PHI, Num(1), PHI, 1 - PHI,
)


# --------------------------------------------------------------------------
# matrices over K (lists of lists)
# --------------------------------------------------------------------------
def mat_eye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def mat_zero(n, m=None):
    m = n if m is None else m
    return [[ZERO for _ in range(m)] for _ in range(n)]


def mat_mul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = []
    for i in range(n):
        row = []
        Ai = A[i]
        for j in range(m):
            s = ZERO
            for t in range(k):
                x = Ai[t]
                if x.is_zero():
                    continue
                y = B[t][j]
                if y.is_zero():
                    continue
                s = s + x * y
            row.append(s)
        out.append(row)
    return out


def mat_add(A, B):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(A, B)]


def mat_scale(A, f):
    return [[x.scale(f) for x in r] for r in A]


def mat_trace(A):
    s = ZERO
    for i in range(len(A)):
        s = s + A[i][i]
    return s


def mat_kron(A, B):
    return [[a * b for a in ra for b in rb] for ra in A for rb in B]


def mat_gal(A):
    return [[x.gal() for x in r] for r in A]


def mat_adjoint(A):
    return [[A[i][j].cconj() for i in range(len(A))] for j in range(len(A[0]))]


def mat_eq(A, B):
    return all(x == y for r, s in zip(A, B) for x, y in zip(r, s))


def mat_is_zero(A):
    return all(x.is_zero() for r in A for x in r)


def mat_encode(A):
    return [[x.encode() for x in r] for r in A]


# --------------------------------------------------------------------------
# Task 1: the group 2I as exact unit quaternions in Q(sqrt5)
# --------------------------------------------------------------------------
def qmul(p, q):
    """Hamilton product, scalar-first (w, x, y, z)."""
    w1, x1, y1, z1 = p
    w2, x2, y2, z2 = q
    return (
        w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
        w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
        w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
        w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
    )


def qconj(q):
    return (q[0], -q[1], -q[2], -q[3])


def qnorm2(q):
    s = ZERO
    for x in q:
        s = s + x * x
    return s


def qkey(q):
    return tuple(x.key() for x in q)


def _parity(perm):
    perm = list(perm)
    sign = 1
    for i in range(len(perm)):
        while perm[i] != i:
            j = perm[i]
            perm[i], perm[j] = perm[j], perm[i]
            sign = -sign
    return sign


def standard_coordinate_families():
    """The 8 + 16 + 96 standard coordinates (as in T031), exact in Q(sqrt5)."""
    half = Fraction(1, 2)
    out = []
    for pos in range(4):                                  # 8 coordinate units
        for s in (1, -1):
            q = [ZERO] * 4
            q[pos] = Num(s)
            out.append(tuple(q))
    for signs in itertools.product((1, -1), repeat=4):    # 16 half-units
        out.append(tuple(Num(s * half) for s in signs))
    base = (ZERO, ONE, PHI, PHI_INV)                      # (0,1,phi,phi^-1)/2
    for perm in itertools.permutations(range(4)):         # 96 even permutations
        if _parity(perm) != 1:
            continue
        for signs in itertools.product((1, -1), repeat=3):
            it = iter(signs)
            q = []
            for p in perm:
                v = base[p]
                q.append(v.scale(half) if v.is_zero() else v.scale(next(it) * half))
            out.append(tuple(q))
    return out


@dataclass
class Group:
    elements: list          # list of quaternion 4-tuples of Num
    index: dict             # qkey -> position
    mul: list               # mul[i][j] = index of elements[i]*elements[j]
    inv: list
    identity: int
    minus_one: int
    gen_s: int              # generator indices
    gen_t: int


def _closure(gens, limit=1000):
    seen = {qkey(g): g for g in gens}
    frontier = list(gens)
    while frontier:
        new = []
        for a in frontier:
            for g in gens:
                p = qmul(a, g)
                k = qkey(p)
                if k not in seen:
                    seen[k] = p
                    new.append(p)
                    if len(seen) > limit:
                        raise ArithmeticError("closure exceeds limit")
        frontier = new
    return seen


def build_group() -> Group:
    fam = standard_coordinate_families()
    by_key = {}
    for q in fam:
        by_key[qkey(q)] = q
    elements = sorted(by_key.values(), key=qkey)
    index = {qkey(q): i for i, q in enumerate(elements)}
    n = len(elements)
    mul = []
    for i in range(n):
        row = []
        for j in range(n):
            k = qkey(qmul(elements[i], elements[j]))
            if k not in index:
                raise ArithmeticError("family not closed under Hamilton product")
            row.append(index[k])
        mul.append(row)
    identity = index[qkey((ONE, ZERO, ZERO, ZERO))]
    minus_one = index[qkey((Num(-1), ZERO, ZERO, ZERO))]
    inv = []
    for i in range(n):
        j = index[qkey(qconj(elements[i]))]
        inv.append(j)
    half = Fraction(1, 2)
    s = (Num(half), Num(half), Num(half), Num(half))
    t = (PHI.scale(half), Num(half), PHI_INV.scale(half), ZERO)
    return Group(elements, index, mul, inv, identity, minus_one,
                 index[qkey(s)], index[qkey(t)])


def element_order(G: Group, i: int) -> int:
    k, x = 1, i
    while x != G.identity:
        x = G.mul[x][i]
        k += 1
    return k


def conjugacy_classes(G: Group):
    n = len(G.elements)
    seen = [False] * n
    classes = []
    for i in range(n):
        if seen[i]:
            continue
        cls = sorted({G.mul[G.mul[g][i]][G.inv[g]] for g in range(n)})
        for x in cls:
            seen[x] = True
        classes.append(cls)
    return classes


def ordered_classes(G: Group):
    """Classes in the fixed nine-class order, matched by (2*Re q = chi_1)."""
    classes = conjugacy_classes(G)
    if len(classes) != 9:
        raise ArithmeticError("expected nine conjugacy classes")
    out = []
    for chi in FUNDAMENTAL_CHARACTER:
        match = [c for c in classes if G.elements[c[0]][0].scale(2) == chi]
        if len(match) != 1:
            raise ArithmeticError("class matching by trace is not unique")
        out.append(match[0])
    return out


def verify_group(G: Group) -> dict:
    n = len(G.elements)
    assert n == ORDER, "cardinality"
    assert len({qkey(q) for q in G.elements}) == n
    for q in G.elements:
        assert qnorm2(q) == ONE, "unit norm"
    # closure was enforced in build_group (every product found in the index);
    # recheck independently as a group generated by two elements
    gens = [G.elements[G.gen_s], G.elements[G.gen_t]]
    gen_set = _closure(gens)
    assert set(gen_set) == {qkey(q) for q in G.elements}, "<s,t> != 2I"
    # identity / inverses / associativity on the exact index table
    for i in range(n):
        assert G.mul[G.identity][i] == i and G.mul[i][G.identity] == i
        assert G.mul[i][G.inv[i]] == G.identity and G.mul[G.inv[i]][i] == G.identity
    mul = G.mul
    for i in range(n):
        mi = mul[i]
        for j in range(n):
            mij = mul[mi[j]]
            mj = mul[j]
            for k in range(n):
                assert mij[k] == mi[mj[k]], "associativity"
    # centre
    centre = [g for g in range(n) if all(mul[g][h] == mul[h][g] for h in range(n))]
    assert sorted(centre) == sorted([G.identity, G.minus_one]), "centre"
    classes = ordered_classes(G)
    sizes = tuple(len(c) for c in classes)
    orders = tuple(element_order(G, c[0]) for c in classes)
    assert sizes == CLASS_SIZES and sum(sizes) == ORDER
    assert orders == CLASS_ORDERS
    for c in classes:  # order constant on classes
        assert len({element_order(G, g) for g in c}) == 1
    return {
        "cardinality": n,
        "associativity_triples_checked": n ** 3,
        "closure_products_checked": n * n,
        "centre": sorted(centre),
        "class_sizes": list(sizes),
        "class_orders": list(orders),
        "generators_generate_group": True,
    }


# --------------------------------------------------------------------------
# Task 2: explicit matrices
# --------------------------------------------------------------------------
def fundamental_matrix(q):
    """q = w+xi+yj+zk -> [[w+xi, y+zi],[-y+zi, w-xi]] (a homomorphism)."""
    w, x, y, z = q
    return [[w + x * I_UNIT, y + z * I_UNIT],
            [-y + z * I_UNIT, w - x * I_UNIT]]


def sym_power(M, k):
    """Sym^k of a 2x2 matrix in the monomial basis v1^{k-j} v2^j (j=0..k).

    M v1 = p v1 + r v2,  M v2 = q v1 + s v2 (column convention); column j of
    the result is the coefficient list of (p + r z)^{k-j} (q + s z)^j in z.
    """
    p, q = M[0][0], M[0][1]
    r, s = M[1][0], M[1][1]
    n = k + 1
    out = mat_zero(n)
    for j in range(n):
        poly = [ONE]
        for _ in range(k - j):
            poly = _poly_mul_lin(poly, p, r)
        for _ in range(j):
            poly = _poly_mul_lin(poly, q, s)
        for l in range(n):
            out[l][j] = poly[l]
    return out


def _poly_mul_lin(poly, c0, c1):
    out = [ZERO] * (len(poly) + 1)
    for i, x in enumerate(poly):
        out[i] = out[i] + x * c0
        out[i + 1] = out[i + 1] + x * c1
    return out


def sym_weights(k):
    """Gram weights of the invariant Hermitian form on Sym^k: 1/C(k,j)."""
    return [Fraction(1, comb(k, j)) for j in range(k + 1)]


@dataclass
class Representation:
    label: str
    dim: int
    construction: str
    matrices: list                      # matrices[g] for g in group index
    weights: list | None = None         # Gram diagonal (None => identity)


def build_representations(G: Group) -> dict:
    n = len(G.elements)
    M2 = [fundamental_matrix(q) for q in G.elements]
    M2p = [mat_gal(m) for m in M2]
    reps = {}
    reps["1"] = Representation("1", 1, "trivial", [[[ONE]] for _ in range(n)])
    reps["2"] = Representation("2", 2, "defining SU(2) representation", M2, [Fraction(1)] * 2)
    reps["2'"] = Representation("2'", 2, "Galois conjugate sigma(2), sigma: sqrt5 -> -sqrt5 entrywise",
                                M2p, [Fraction(1)] * 2)
    reps["3"] = Representation("3", 3, "Sym^2(2)", [sym_power(m, 2) for m in M2], sym_weights(2))
    reps["3'"] = Representation("3'", 3, "Sym^2(2')", [sym_power(m, 2) for m in M2p], sym_weights(2))
    reps["4"] = Representation("4", 4, "tensor product 2 (x) 2'",
                               [mat_kron(a, b) for a, b in zip(M2, M2p)], [Fraction(1)] * 4)
    reps["4'"] = Representation("4'", 4, "Sym^3(2)", [sym_power(m, 3) for m in M2], sym_weights(3))
    reps["5"] = Representation("5", 5, "Sym^4(2)", [sym_power(m, 4) for m in M2], sym_weights(4))
    reps["6"] = Representation("6", 6, "Sym^5(2)", [sym_power(m, 5) for m in M2], sym_weights(5))
    return reps


def symmetric_power_rep(G: Group, k: int):
    return [sym_power(fundamental_matrix(q), k) for q in G.elements]


def verify_homomorphism(G: Group, mats: list, sample_pairs: int = 300, seed: int = 34) -> dict:
    """Exact proof that g -> mats[g] is a homomorphism.

    Cayley-graph argument: if mats[e] = I and mats[g x] = mats[g] mats[x] for
    every g in G and every x in a generating set, then by induction on word
    length mats[g w] = mats[g] mats[w] for every word w, i.e. for every h in G.
    A deterministic random sample of full products is added as a redundant
    check.
    """
    n = len(G.elements)
    dim = len(mats[0])
    assert mat_eq(mats[G.identity], mat_eye(dim)), "identity"
    for x in (G.gen_s, G.gen_t):
        for g in range(n):
            assert mat_eq(mats[G.mul[g][x]], mat_mul(mats[g], mats[x])), "edge"
    rng = random.Random(seed)
    for _ in range(sample_pairs):
        g, h = rng.randrange(n), rng.randrange(n)
        assert mat_eq(mats[G.mul[g][h]], mat_mul(mats[g], mats[h])), "sample"
    return {"edges_checked": 2 * n, "sample_pairs": sample_pairs}


def verify_weighted_unitarity(G: Group, rep: Representation) -> bool:
    """rho(g)^* D rho(g) = D with D = diag(weights) (exact)."""
    d = rep.dim
    D = [[Num(rep.weights[i]) if i == j else ZERO for j in range(d)] for i in range(d)]
    for m in rep.matrices:
        lhs = mat_mul(mat_adjoint(m), mat_mul(D, m))
        if not mat_eq(lhs, D):
            return False
    return True


def galois_compatibility(G: Group, reps: dict) -> dict:
    """Why 2' = sigma(2) is a representation, and what sigma does NOT do.

    * sigma is a ring automorphism of K, hence entrywise sigma is a ring
      automorphism of M_n(K); so g -> sigma(rho(g)) is a homomorphism of the
      abstract group (checked exactly via verify_homomorphism).
    * It does NOT map the set 2I (as quaternions) to itself: sigma(2I) is the
      other conjugate icosahedral subgroup of SU(2).  We count how many sigma(g)
      lie in 2I.
    * Defining relations on the generators s (order 6) and t (order 10) are
      checked directly on sigma(rho(s)), sigma(rho(t)).
    """
    mats = reps["2'"].matrices
    verify_homomorphism(G, mats)
    inside = sum(1 for q in G.elements
                 if qkey(tuple(x.gal() for x in q)) in G.index)
    s, t = G.gen_s, G.gen_t
    ms, mt = mats[s], mats[t]
    I2 = mat_eye(2)
    minus = mat_scale(I2, -1)

    def power(m, k):
        out = mat_eye(len(m))
        for _ in range(k):
            out = mat_mul(out, m)
        return out

    st = G.mul[s][t]
    ord_s, ord_t, ord_st = element_order(G, s), element_order(G, t), element_order(G, st)
    rel = {
        f"s^{ord_s}=I": mat_eq(power(ms, ord_s), I2),
        f"t^{ord_t}=I": mat_eq(power(mt, ord_t), I2),
        f"(st)^{ord_st}=I": mat_eq(power(mat_mul(ms, mt), ord_st), I2),
        f"s^{ord_s // 2}=-I": mat_eq(power(ms, ord_s // 2), minus),
        f"t^{ord_t // 2}=-I": mat_eq(power(mt, ord_t // 2), minus),
    }
    assert all(rel.values()), rel
    return {"sigma_of_2I_inside_2I": inside, "group_order": ORDER,
            "sigma_preserves_set_2I": inside == ORDER, "relations": rel}


# --------------------------------------------------------------------------
# Task 3: characters, orthogonality
# --------------------------------------------------------------------------
def characters_from_matrices(G: Group, reps: dict):
    """Character table, computed from the matrices on all 120 elements."""
    classes = ordered_classes(G)
    table = {}
    for label, rep in reps.items():
        values = []
        for cls in classes:
            tr = [mat_trace(rep.matrices[g]) for g in cls]
            assert all(x == tr[0] for x in tr), f"character not constant on class ({label})"
            values.append(tr[0])
        table[label] = tuple(values)
    return table, classes


def verify_character_table(table: dict) -> dict:
    labels = LABELS
    assert set(table) == set(labels)
    for l in labels:
        assert table[l][0] == IRREP_DIMENSIONS[l]
        assert all(x.is_real() for x in table[l]), "characters are real"
    assert sum(CLASS_SIZES) == ORDER
    assert sum(IRREP_DIMENSIONS[l] ** 2 for l in labels) == ORDER
    # row orthogonality (irreducibility: norm 1; inequivalence: off-diagonal 0)
    for a in labels:
        for b in labels:
            s = ZERO
            for j in range(9):
                s = s + (table[a][j].cconj() * table[b][j]).scale(CLASS_SIZES[j])
            assert s.scale(Fraction(1, ORDER)) == (1 if a == b else 0), (a, b)
    # column orthogonality
    for j in range(9):
        for k in range(9):
            s = ZERO
            for l in labels:
                s = s + table[l][j].cconj() * table[l][k]
            expected = Fraction(ORDER, CLASS_SIZES[j]) if j == k else 0
            assert s == expected, (j, k)
    # regular character: sum_rho d_rho chi_rho(C) = 120 delta_{C,1}
    for j in range(9):
        s = ZERO
        for l in labels:
            s = s + table[l][j].scale(IRREP_DIMENSIONS[l])
        assert s == (ORDER if j == 0 else 0)
    assert tuple(table["2"]) == FUNDAMENTAL_CHARACTER
    return {"row_pairs": 81, "column_pairs": 81}


# --------------------------------------------------------------------------
# Schur orthogonality of matrix coefficients (proof of matrix units)
# --------------------------------------------------------------------------
def verify_schur_orthogonality(G: Group, reps: dict, labels=LABELS) -> int:
    """(d_r/120) sum_g rho(g)_{ij} sigma(g^{-1})_{kl} = delta_{rs} delta_{il} delta_{jk}."""
    count = 0
    n = len(G.elements)
    for a in labels:
        ra = reps[a]
        for b in labels:
            rb = reps[b]
            for i in range(ra.dim):
                for j in range(ra.dim):
                    for k in range(rb.dim):
                        for l in range(rb.dim):
                            s = ZERO
                            for g in range(n):
                                x = ra.matrices[g][i][j]
                                if x.is_zero():
                                    continue
                                y = rb.matrices[G.inv[g]][k][l]
                                if y.is_zero():
                                    continue
                                s = s + x * y
                            val = s.scale(Fraction(ra.dim, ORDER))
                            expected = 1 if (a == b and i == l and j == k) else 0
                            assert val == expected, (a, b, i, j, k, l)
                            count += 1
    return count


# --------------------------------------------------------------------------
# Task 4: projectors and matrix units on Sym^m(2)
# --------------------------------------------------------------------------
def central_projector(G: Group, chi: tuple, classes, d: int, U: list):
    """P = (d/120) sum_g conj(chi(g)) U(g)."""
    class_of = {}
    for j, cls in enumerate(classes):
        for g in cls:
            class_of[g] = j
    dim = len(U[0])
    acc = mat_zero(dim)
    for g in range(len(G.elements)):
        c = chi[class_of[g]].cconj()
        if c.is_zero():
            continue
        acc = mat_add(acc, [[x * c for x in r] for r in U[g]])
    return mat_scale(acc, Fraction(d, ORDER))


def matrix_unit(G: Group, rep: Representation, i: int, j: int, U: list):
    """E_ij = (d/120) sum_g rho(g^{-1})_{ji} U(g)  (basis-independent form)."""
    dim = len(U[0])
    acc = mat_zero(dim)
    for g in range(len(G.elements)):
        c = rep.matrices[G.inv[g]][j][i]
        if c.is_zero():
            continue
        acc = mat_add(acc, [[x * c for x in r] for r in U[g]])
    return mat_scale(acc, Fraction(rep.dim, ORDER))


def verify_projectors_on_sym(G: Group, table: dict, classes, m: int,
                             full_orthogonality: bool, U: list | None = None) -> dict:
    U = U if U is not None else symmetric_power_rep(G, m)
    dim = m + 1
    P = {l: central_projector(G, table[l], classes, IRREP_DIMENSIONS[l], U) for l in LABELS}
    ranks = {}
    for l in LABELS:
        assert mat_eq(mat_mul(P[l], P[l]), P[l]), f"idempotent {l} m={m}"
        tr = mat_trace(P[l])
        assert tr.is_real() and tr.b == 0 and tr.a.denominator == 1
        ranks[l] = int(tr.a)       # idempotent => rank = trace
        assert ranks[l] == IRREP_DIMENSIONS[l] * molien_coefficients(l, m)[m], (l, m)
        # commutes with U(g)
    total = mat_zero(dim)
    for l in LABELS:
        total = mat_add(total, P[l])
    assert mat_eq(total, mat_eye(dim)), f"sum of projectors m={m}"
    assert sum(ranks.values()) == dim
    pairs = 0
    if full_orthogonality:
        for a, b in itertools.combinations(LABELS, 2):
            assert mat_is_zero(mat_mul(P[a], P[b])), (a, b, m)
            assert mat_is_zero(mat_mul(P[b], P[a])), (b, a, m)
            pairs += 1
        # central: commute with a generator pair
        for l in LABELS:
            for g in (G.gen_s, G.gen_t):
                assert mat_eq(mat_mul(P[l], U[g]), mat_mul(U[g], P[l]))
    return {"m": m, "ranks": ranks, "orthogonal_pairs": pairs}


def block_diagonal(mats_list):
    """Direct sum of several families of matrices (indexed by group element)."""
    out = []
    for g in range(len(mats_list[0])):
        blocks = [m[g] for m in mats_list]
        dim = sum(len(b) for b in blocks)
        M = mat_zero(dim)
        off = 0
        for b in blocks:
            for i, row in enumerate(b):
                for j, x in enumerate(row):
                    M[off + i][off + j] = x
            off += len(b)
        out.append(M)
    return out


def verify_matrix_units(G: Group, reps: dict, U: list, multiplicity: dict,
                        sample: int = 60, seed: int = 7) -> dict:
    """Matrix-unit identities on a representation U with known multiplicities.

    Checks, for each listed irrep: E_ii idempotent of trace = multiplicity m_rho,
    sum_i E_ii has trace d*m_rho (= rank of the central projector), and the
    multiplication rule E_ij E_kl = delta_jk E_il on a deterministic sample
    (all index quadruples when there are at most `sample` of them).
    """
    dim = len(U[0])
    rng = random.Random(seed)
    checked = 0
    for l, b in multiplicity.items():
        rep = reps[l]
        d = rep.dim
        E = {(i, j): matrix_unit(G, rep, i, j, U) for i in range(d) for j in range(d)}
        diag = mat_zero(dim)
        for i in range(d):
            diag = mat_add(diag, E[(i, i)])
            assert mat_eq(mat_mul(E[(i, i)], E[(i, i)]), E[(i, i)])
            assert mat_trace(E[(i, i)]) == b, (l, i, b)     # dim of multiplicity space
            checked += 1
        assert mat_trace(diag) == d * b
        quads = [(i, j, k, ll) for i in range(d) for j in range(d)
                 for k in range(d) for ll in range(d)]
        if len(quads) > sample:
            quads = rng.sample(quads, sample)
        for (i, j, k, ll) in quads:
            lhs = mat_mul(E[(i, j)], E[(k, ll)])
            rhs = E[(i, ll)] if j == k else mat_zero(dim)
            assert mat_eq(lhs, rhs), (l, i, j, k, ll)
            checked += 1
        # equivariance: U(g) E_{i1} = sum_j rho(g)_{ji} E_{j1}  (transport of the basis)
        for g in (G.gen_s, G.gen_t):
            for i in range(d):
                lhs = mat_mul(U[g], E[(i, 0)])
                rhs = mat_zero(dim)
                for j in range(d):
                    rhs = mat_add(rhs, [[x * rep.matrices[g][j][i] for x in r] for r in E[(j, 0)]])
                assert mat_eq(lhs, rhs), (l, g, i)
                checked += 1
    return {"multiplicities": dict(multiplicity), "identities_checked": checked}


def verify_matrix_units_on_sym(G: Group, reps: dict, m: int, labels=LABELS,
                               sample: int = 60, seed: int = 7) -> dict:
    """Matrix units on Sym^m(2); multiplicities taken from the T032 Molien data."""
    U = symmetric_power_rep(G, m)
    mult = {l: molien_coefficients(l, m)[m] for l in labels if molien_coefficients(l, m)[m] > 0}
    r = verify_matrix_units(G, reps, U, mult, sample, seed)
    r["m"] = m
    return r


def verify_matrix_units_multiplicity_two(G: Group, reps: dict) -> dict:
    """Sym^2 + Sym^10 contains the 3 twice: genuinely multiplicity-two matrix units."""
    U = block_diagonal([symmetric_power_rep(G, 2), symmetric_power_rep(G, 10)])
    return verify_matrix_units(G, reps, U, {"3": 2})


# --------------------------------------------------------------------------
# Task 5: Molien series from characters, as an exact rational-function identity
# --------------------------------------------------------------------------
def poly_trim(p):
    p = list(p)
    while p and p[-1].is_zero():
        p.pop()
    return p


def poly_add(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else ZERO) + (q[i] if i < len(q) else ZERO) for i in range(n)]


def poly_mul(p, q):
    out = [ZERO] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] = out[i + j] + x * y
    return out


def poly_div_monic(p, q):
    """exact division by a monic divisor; returns (quotient, remainder)."""
    p = list(p)
    dq = len(q) - 1
    assert q[-1] == ONE
    quo = [ZERO] * max(len(p) - dq, 1)
    for i in range(len(p) - 1, dq - 1, -1):
        c = p[i]
        if c.is_zero():
            continue
        quo[i - dq] = c
        for j in range(dq + 1):
            p[i - dq + j] = p[i - dq + j] - c * q[j]
    return quo, poly_trim(p)


def molien_denominator():
    one_minus_12 = [ONE] + [ZERO] * 11 + [Num(-1)]
    one_minus_20 = [ONE] + [ZERO] * 19 + [Num(-1)]
    return poly_mul(one_minus_12, one_minus_20)


def class_quotients():
    """D(t)/q_C(t) with q_C(t) = 1 - chi_1(C) t + t^2 = det(1 - t g); exact polynomials."""
    D = molien_denominator()
    out = []
    for chi in FUNDAMENTAL_CHARACTER:
        q = [ONE, -chi, ONE]
        quo, rem = poly_div_monic(D, q)
        assert rem == [], "q_C does not divide (1-t^12)(1-t^20)"
        out.append(quo)
    return out


def numerator_from_characters(table: dict, label: str):
    """N_rho(t) := (1-t^12)(1-t^20) * (1/120) sum_C |C| conj(chi_rho(C)) / q_C(t)."""
    quos = class_quotients()
    acc = []
    for j in range(9):
        w = table[label][j].cconj().scale(Fraction(CLASS_SIZES[j], ORDER))
        acc = poly_add(acc, [c * w for c in quos[j]])
    return poly_trim(acc)


def numerator_from_t021(label: str):
    support = IRREP_NUMERATORS[label]
    top = max(support)
    coeffs = [ZERO] * (top + 1)
    for e in support:
        coeffs[e] = coeffs[e] + ONE
    return poly_trim(coeffs)


def verify_molien_exact(table: dict) -> dict:
    """For every irrep: character-side Molien numerator == T021/T032 numerator.

    sum_m <chi_rho, chi_{Sym^m}> t^m = (1/120) sum_C |C| conj chi_rho(C)/q_C(t)
    because sum_m chi_{Sym^m}(g) t^m = 1/det(1-tg).  Equality of the two
    numerators over the common denominator (1-t^12)(1-t^20) is therefore an
    all-degree identity, not a finite regression test.
    """
    for l in LABELS:
        mine = numerator_from_characters(table, l)
        theirs = numerator_from_t021(l)
        assert len(mine) == len(theirs) and all(x == y for x, y in zip(mine, theirs)), l
    # sum_rho d_rho N_rho = (1-t^12)(1-t^20)/(1-t)^2  =>  sum d M = 1/(1-t)^2
    total = []
    for l in LABELS:
        total = poly_add(total, [c.scale(IRREP_DIMENSIONS[l]) for c in numerator_from_t021(l)])
    D = molien_denominator()
    quo, rem = poly_div_monic(D, [ONE, Num(-2), ONE])
    assert rem == []
    total, quo = poly_trim(total), poly_trim(quo)
    assert len(total) == len(quo) and all(x == y for x, y in zip(total, quo))
    return {"numerators_checked": 9, "degree_of_common_denominator": len(D) - 1}


def verify_character_average_series(table: dict, max_degree: int = 240) -> int:
    """Finite cross-check: <chi_rho, chi_m> = b_{m,rho} for m <= max_degree (exact)."""
    chars = [[ONE] * 9, list(FUNDAMENTAL_CHARACTER)]
    for m in range(2, max_degree + 1):
        chars.append([FUNDAMENTAL_CHARACTER[j] * chars[m - 1][j] - chars[m - 2][j] for j in range(9)])
    checked = 0
    for l in LABELS:
        b = molien_coefficients(l, max_degree)
        for m in range(max_degree + 1):
            s = ZERO
            for j in range(9):
                s = s + (table[l][j].cconj() * chars[m][j]).scale(CLASS_SIZES[j])
            assert s.scale(Fraction(1, ORDER)) == b[m], (l, m)
            checked += 1
    return checked


def cover_level_multiplicities(max_degree: int = 60) -> bool:
    """Peter-Weyl bookkeeping (T031/T033): at level m of L^2(S^3) the
    rho-equivariant functions u(gq)=rho(g)u(q) form a space of dimension
    (m+1) b_{m,rho}; with weights d_rho they add up to (m+1)^2 = dim of level m."""
    for m in range(max_degree + 1):
        total = sum(IRREP_DIMENSIONS[l] * (m + 1) * molien_coefficients(l, m)[m] for l in LABELS)
        if total != (m + 1) ** 2:
            return False
    return True


# --------------------------------------------------------------------------
# export
# --------------------------------------------------------------------------
def q5_str(x: Num) -> str:
    assert x.is_real()
    if x.b == 0:
        return str(x.a)
    if x.a == 0:
        return f"({x.b})*sqrt5"
    return f"{x.a}+({x.b})*sqrt5"


def export_json(G: Group, reps: dict, table: dict, classes, report: dict) -> dict:
    return {
        "group": "binary_icosahedral_group_2I",
        "order": ORDER,
        "encoding": "algebraic number [a,b,c,d] (strings of rationals) means a+b*sqrt5+(c+d*sqrt5)*i; "
                    "character values are real so c=d=0 and are also given as 'values_text'",
        "character_field": "Q(sqrt5)",
        "matrix_field": "Q(sqrt5, i)",
        "quaternion_convention": "scalar-first (w,x,y,z), Hamilton product, left deck action g q",
        "class_order": list(range(9)),
        "class_sizes": list(CLASS_SIZES),
        "class_element_orders": list(CLASS_ORDERS),
        "class_representatives": [[q5_str(x) for x in G.elements[c[0]]] for c in classes],
        "fundamental_character": [q5_str(x) for x in FUNDAMENTAL_CHARACTER],
        "irreps": {
            l: {
                "dimension": reps[l].dim,
                "construction": reps[l].construction,
                "faithful_spinorial": bool(table[l][1] == -reps[l].dim),
                "values": [x.encode() for x in table[l]],
                "values_text": [q5_str(x) for x in table[l]],
                "generator_matrices": {
                    "s": {"quaternion": [q5_str(x) for x in G.elements[G.gen_s]],
                          "matrix": mat_encode(reps[l].matrices[G.gen_s])},
                    "t": {"quaternion": [q5_str(x) for x in G.elements[G.gen_t]],
                          "matrix": mat_encode(reps[l].matrices[G.gen_t])},
                },
            }
            for l in LABELS
        },
        "verification": report,
    }


def run_all(verbose: bool = False, molien_sym_max: int = 13) -> tuple:
    G = build_group()
    report = {"group": verify_group(G)}
    reps = build_representations(G)
    hom = {}
    for l in LABELS:
        hom[l] = verify_homomorphism(G, reps[l].matrices)
        assert len(reps[l].matrices[0]) == IRREP_DIMENSIONS[l]
    report["homomorphism"] = hom
    report["weighted_unitarity"] = {
        l: verify_weighted_unitarity(G, reps[l]) for l in LABELS if reps[l].weights}
    assert all(report["weighted_unitarity"].values())
    report["galois"] = galois_compatibility(G, reps)
    table, classes = characters_from_matrices(G, reps)
    report["character_table"] = verify_character_table(table)
    report["molien_all_degrees"] = verify_molien_exact(table)
    report["molien_finite_average_checks"] = verify_character_average_series(table, 240)
    report["peter_weyl_level_sum"] = cover_level_multiplicities()
    assert report["peter_weyl_level_sum"]
    report["schur_orthogonality_entries"] = verify_schur_orthogonality(G, reps)
    proj = []
    for m in range(molien_sym_max + 1):
        proj.append(verify_projectors_on_sym(G, table, classes, m, full_orthogonality=(m <= 7)))
    report["projectors_on_sym"] = proj
    mu = [verify_matrix_units_on_sym(G, reps, m) for m in range(8)]
    mu.append(verify_matrix_units_multiplicity_two(G, reps))
    report["matrix_units_on_sym"] = mu
    return G, reps, table, classes, report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="data/t034_2i_character_table.json")
    args = parser.parse_args()
    G, reps, table, classes, report = run_all()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = export_json(G, reps, table, classes, report)
    out.write_text(json.dumps(payload, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "output": str(out)}, indent=1))


if __name__ == "__main__":
    main()

"""T034 unico, autocontenuto, ottimizzato e completo per Kaggle.

Aritmetica esatta in Q(sqrt5)[i] con fractions.Fraction. Nessuna dipendenza
da sympy o da repository esterni. Il modulo T032 (numeratori di Molien) è
incorporato sotto.
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

# ==========================================================================
# T032 incorporato: numeratori di Molien dei covarianti di 2I
# ==========================================================================
IRREP_NUMERATORS = {
    "1": (0, 30), "2": (1, 11, 19, 29), "2'": (7, 13, 17, 23),
    "3": (2, 10, 12, 18, 20, 28), "3'": (6, 10, 14, 16, 20, 24),
    "4": (6, 8, 12, 14, 16, 18, 22, 24),
    "4'": (3, 9, 11, 13, 17, 19, 21, 27),
    "5": (4, 8, 10, 12, 14, 16, 18, 20, 22, 26),
    "6": (5, 7, 9, 11, 13, 15, 15, 17, 19, 21, 23, 25),
}
IRREP_DIMENSIONS = {"1": 1, "2": 2, "2'": 2, "3": 3, "3'": 3,
                    "4": 4, "4'": 4, "5": 5, "6": 6}


def molien_coefficients(label: str, max_degree: int) -> tuple:
    """Coefficienti di N(t)/((1-t^12)(1-t^20)) fino a max_degree."""
    if label not in IRREP_NUMERATORS:
        raise KeyError(label)
    support = IRREP_NUMERATORS[label]
    out = []
    for m in range(max_degree + 1):
        c = 0
        for e in support:
            r = m - e
            if r < 0:
                continue
            for a in range(r // 12 + 1):
                rem = r - 12 * a
                if rem % 20 == 0:
                    c += 1
        out.append(c)
    return tuple(out)


# ==========================================================================
# Campo K = Q(sqrt5)[i]:  a + b*sqrt5 + (c + d*sqrt5)*i
# ==========================================================================
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
        return Num(self.a, self.b, -self.c, -self.d)

    def gal(self):
        """sqrt5 -> -sqrt5, i fisso."""
        return Num(self.a, -self.b, self.c, self.d)

    def is_zero(self):
        return self.a == 0 and self.b == 0 and self.c == 0 and self.d == 0

    def is_real(self):
        return self.c == 0 and self.d == 0

    def key(self):
        return (self.a, self.b, self.c, self.d)

    def __eq__(self, o):
        if not isinstance(o, (Num, int, Fraction)):
            return NotImplemented
        return self.key() == Num.of(o).key()

    def __hash__(self):
        return hash(self.key())

    def encode(self):
        return [str(self.a), str(self.b), str(self.c), str(self.d)]

    def __repr__(self):
        parts = []
        if self.a != 0 or self.is_zero():
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
PHI = Num(Fraction(1, 2), Fraction(1, 2))
PHI_INV = PHI - 1

FUNDAMENTAL_CHARACTER = (
    Num(2), Num(-2), Num(-1), Num(0),
    PHI - 1, -PHI, Num(1), PHI, 1 - PHI,
)


# ==========================================================================
# Matrici su K
# ==========================================================================
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
        for j in range(m):
            s = ZERO
            for t in range(k):
                x, y = A[i][t], B[t][j]
                if x.is_zero() or y.is_zero():
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


# ==========================================================================
# Gruppo 2I come quaternioni esatti
# ==========================================================================
def qmul(p, q):
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
    half = Fraction(1, 2)
    out = []
    for pos in range(4):
        for s in (1, -1):
            q = [ZERO] * 4
            q[pos] = Num(s)
            out.append(tuple(q))
    for signs in itertools.product((1, -1), repeat=4):
        out.append(tuple(Num(s * half) for s in signs))
    base = (ZERO, ONE, PHI, PHI_INV)
    for perm in itertools.permutations(range(4)):
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
    elements: list
    index: dict
    mul: list
    inv: list
    identity: int
    minus_one: int
    gen_s: int
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
    by_key = {}
    for q in standard_coordinate_families():
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
                raise ArithmeticError("famiglia non chiusa sotto il prodotto")
            row.append(index[k])
        mul.append(row)
    identity = index[qkey((ONE, ZERO, ZERO, ZERO))]
    minus_one = index[qkey((Num(-1), ZERO, ZERO, ZERO))]
    inv = [index[qkey(qconj(elements[i]))] for i in range(n)]
    half = Fraction(1, 2)
    s = (Num(half), Num(half), Num(half), Num(half))
    t = (PHI.scale(half), Num(half), PHI_INV.scale(half), ZERO)
    return Group(elements, index, mul, inv, identity, minus_one,
                 index[qkey(s)], index[qkey(t)])


def element_order(G, i):
    k, x = 1, i
    while x != G.identity:
        x = G.mul[x][i]
        k += 1
    return k


def conjugacy_classes(G):
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


def ordered_classes(G):
    classes = conjugacy_classes(G)
    if len(classes) != 9:
        raise ArithmeticError("attese nove classi di coniugio")
    out = []
    for chi in FUNDAMENTAL_CHARACTER:
        match = [c for c in classes if G.elements[c[0]][0].scale(2) == chi]
        if len(match) != 1:
            raise ArithmeticError("abbinamento classi per traccia non unico")
        out.append(match[0])
    return out


CLASS_SIZES = (1, 1, 20, 30, 12, 12, 20, 12, 12)
CLASS_ORDERS = (1, 2, 3, 4, 5, 5, 6, 10, 10)
LABELS = ("1", "2", "2'", "3", "3'", "4", "4'", "5", "6")


def verify_group(G) -> dict:
    n = len(G.elements)
    assert n == 120, "cardinalità"
    assert len({qkey(q) for q in G.elements}) == n
    for q in G.elements:
        assert qnorm2(q) == ONE, "norma unitaria"
    gen_set = _closure([G.elements[G.gen_s], G.elements[G.gen_t]])
    assert set(gen_set) == {qkey(q) for q in G.elements}, "<s,t> != 2I"
    for i in range(n):
        assert G.mul[G.identity][i] == i and G.mul[i][G.identity] == i
        assert G.mul[i][G.inv[i]] == G.identity and G.mul[G.inv[i]][i] == G.identity
    mul = G.mul
    centre = [g for g in range(n) if all(mul[g][h] == mul[h][g] for h in range(n))]
    assert sorted(centre) == sorted([G.identity, G.minus_one]), "centro"
    classes = ordered_classes(G)
    sizes = tuple(len(c) for c in classes)
    orders = tuple(element_order(G, c[0]) for c in classes)
    assert sizes == CLASS_SIZES and sum(sizes) == 120
    assert orders == CLASS_ORDERS
    for c in classes:
        assert len({element_order(G, g) for g in c}) == 1
    return {"cardinality": n, "centre": sorted(centre),
            "class_sizes": list(sizes), "class_orders": list(orders)}


# ==========================================================================
# Rappresentazioni
# ==========================================================================
def fundamental_matrix(q):
    w, x, y, z = q
    return [[w + x * I_UNIT, y + z * I_UNIT],
            [-y + z * I_UNIT, w - x * I_UNIT]]


def _poly_mul_lin(poly, c0, c1):
    out = [ZERO] * (len(poly) + 1)
    for i, x in enumerate(poly):
        out[i] = out[i] + x * c0
        out[i + 1] = out[i + 1] + x * c1
    return out


def sym_power(M, k):
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


def sym_weights(k):
    return [Fraction(1, comb(k, j)) for j in range(k + 1)]


@dataclass
class Representation:
    label: str
    dim: int
    construction: str
    matrices: list
    weights: list | None = None


def build_representations(G):
    n = len(G.elements)
    M2 = [fundamental_matrix(q) for q in G.elements]
    
    def q_gal(q):
        return tuple(x.gal() for x in q)
    
    M2p = [fundamental_matrix(q_gal(q)) for q in G.elements]

    reps = {}
    reps["1"] = Representation("1", 1, "trivial", [[[ONE]] for _ in range(n)])
    reps["2"] = Representation("2", 2, "defining SU(2)", M2, [Fraction(1)] * 2)
    reps["2'"] = Representation("2'", 2, "sigma(2)", M2p, [Fraction(1)] * 2)
    reps["3"] = Representation("3", 3, "Sym^2(2)", [sym_power(m, 2) for m in M2], sym_weights(2))
    reps["3'"] = Representation("3'", 3, "Sym^2(2')", [sym_power(m, 2) for m in M2p], sym_weights(2))
    reps["4"] = Representation("4", 4, "2 (x) 2'",
                            [mat_kron(a, b) for a, b in zip(M2, M2p)], [Fraction(1)] * 4)
    reps["4'"] = Representation("4'", 4, "Sym^3(2)", [sym_power(m, 3) for m in M2], sym_weights(3))
    reps["5"] = Representation("5", 5, "Sym^4(2)", [sym_power(m, 4) for m in M2], sym_weights(4))
    reps["6"] = Representation("6", 6, "Sym^5(2)", [sym_power(m, 5) for m in M2], sym_weights(5))
    return reps


def symmetric_power_rep(G, k):
    return [sym_power(fundamental_matrix(q), k) for q in G.elements]


def verify_homomorphism(G, mats, sample_pairs=100, seed=34):
    n = len(G.elements)
    dim = len(mats[0])
    assert mat_eq(mats[G.identity], mat_eye(dim)), "identità"
    for x in (G.gen_s, G.gen_t):
        for g in range(n):
            assert mat_eq(mats[G.mul[g][x]], mat_mul(mats[g], mats[x])), "spigolo"
    rng = random.Random(seed)
    for _ in range(sample_pairs):
        g, h = rng.randrange(n), rng.randrange(n)
        assert mat_eq(mats[G.mul[g][h]], mat_mul(mats[g], mats[h])), "campione"
    return {"edges_checked": 2 * n, "sample_pairs": sample_pairs}


def verify_homomorphism_detects_error(G, mats):
    bad = [list(map(list, m)) for m in mats]
    bad[G.gen_s] = mat_scale(bad[G.gen_s], 2)
    try:
        verify_homomorphism(G, bad, sample_pairs=20)
    except AssertionError:
        return True
    raise AssertionError("il controllo non rileva una mappa sbagliata")


def verify_weighted_unitarity(rep):
    d = rep.dim
    D = [[Num(rep.weights[i]) if i == j else ZERO for j in range(d)] for i in range(d)]
    for m in rep.matrices:
        if not mat_eq(mat_mul(mat_adjoint(m), mat_mul(D, m)), D):
            return False
    return True


def galois_compatibility(G, reps):
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

    ord_s, ord_t, ord_st = element_order(G, s), element_order(G, t), element_order(G, G.mul[s][t])
    rel = {
        f"s^{ord_s}=I": mat_eq(power(ms, ord_s), I2),
        f"t^{ord_t}=I": mat_eq(power(mt, ord_t), I2),
        f"s^{ord_s//2}=-I": mat_eq(power(ms, ord_s // 2), minus),
        f"t^{ord_t//2}=-I": mat_eq(power(mt, ord_t // 2), minus),
    }
    assert all(rel.values()), rel
    return {"sigma_of_2I_inside_2I": inside, "sigma_preserves_2I": inside == 120, "relations": rel}


def mat_trace_class(rep, G, classes):
    table = {}
    for label, r in rep.items():
        values = []
        for cls in classes:
            tr = [mat_trace(r.matrices[g]) for g in cls]
            assert all(x == tr[0] for x in tr), f"carattere non costante ({label})"
            values.append(tr[0])
        table[label] = tuple(values)
    return table


def verify_character_table(table):
    for l in LABELS:
        assert table[l][0] == IRREP_DIMENSIONS[l]
        assert all(x.is_real() for x in table[l]), "caratteri reali"
    for a in LABELS:
        for b in LABELS:
            s = ZERO
            for j in range(9):
                s = s + (table[a][j].cconj() * table[b][j]).scale(CLASS_SIZES[j])
            assert s.scale(Fraction(1, 120)) == (1 if a == b else 0), (a, b)
    return {"row_pairs": 81, "column_pairs": 81}


def multiplicity_in_sym(table, classes, m):
    chars = [[ONE] * 9, list(FUNDAMENTAL_CHARACTER)]
    for k in range(2, m + 1):
        chars.append([FUNDAMENTAL_CHARACTER[j] * chars[k - 1][j] - chars[k - 2][j] for j in range(9)])
    out = {}
    for l in LABELS:
        s = ZERO
        for j in range(9):
            s = s + (table[l][j].cconj() * chars[m][j]).scale(CLASS_SIZES[j])
        out[l] = int(s.scale(Fraction(1, 120)).a)
    return out


def verify_multiplicities_vs_molien(table, classes, max_m=60):
    checked = 0
    for m in range(max_m + 1):
        mult = multiplicity_in_sym(table, classes, m)
        for l in LABELS:
            assert mult[l] == molien_coefficients(l, m)[m], (l, m)
            checked += 1
    return checked


def verify_projector_rank_on_sym(table, classes, m):
    mult = multiplicity_in_sym(table, classes, m)
    return {l: IRREP_DIMENSIONS[l] * mult[l] for l in LABELS}


def verify_schur_orthogonality(G, reps):
    count = 0
    n = len(G.elements)
    for a in LABELS:
        ra = reps[a]
        for b in LABELS:
            rb = reps[b]
            for i in range(ra.dim):
                for j in range(ra.dim):
                    for k in range(rb.dim):
                        for l in range(rb.dim):
                            s = ZERO
                            for g in range(n):
                                x = ra.matrices[g][i][j]
                                y = rb.matrices[G.inv[g]][k][l]
                                if x.is_zero() or y.is_zero():
                                    continue
                                s = s + x * y
                            val = s.scale(Fraction(ra.dim, 120))
                            expected = 1 if (a == b and i == l and j == k) else 0
                            assert val == expected, (a, b, i, j, k, l)
                            count += 1
    return count


def central_projector(G, chi, classes, d, U):
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
    return mat_scale(acc, Fraction(d, 120))


def matrix_unit(G, rep, i, j, U):
    dim = len(U[0])
    acc = mat_zero(dim)
    for g in range(len(G.elements)):
        c = rep.matrices[G.inv[g]][j][i]
        if c.is_zero():
            continue
        acc = mat_add(acc, [[x * c for x in r] for r in U[g]])
    return mat_scale(acc, Fraction(rep.dim, 120))


def verify_projectors_on_sym(G, table, classes, m, full_orthogonality):
    U = symmetric_power_rep(G, m)
    dim = m + 1
    P = {l: central_projector(G, table[l], classes, IRREP_DIMENSIONS[l], U) for l in LABELS}
    expected = verify_projector_rank_on_sym(table, classes, m)
    ranks = {}
    for l in LABELS:
        assert mat_eq(mat_mul(P[l], P[l]), P[l]), f"idempotente {l} m={m}"
        tr = mat_trace(P[l])
        ranks[l] = int(tr.a)
        assert ranks[l] == expected[l], (l, m, ranks[l], expected[l])
    total = mat_zero(dim)
    for l in LABELS:
        total = mat_add(total, P[l])
    assert mat_eq(total, mat_eye(dim)), f"somma proiettori m={m}"
    pairs = 0
    if full_orthogonality:
        for a, b in itertools.combinations(LABELS, 2):
            assert mat_is_zero(mat_mul(P[a], P[b])), (a, b, m)
            pairs += 1
    return {"m": m, "ranks": ranks, "orthogonal_pairs": pairs}


def block_diagonal(mats_list):
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


def verify_matrix_units(G, reps, U, multiplicity, sample=30, seed=7):
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
            assert mat_trace(E[(i, i)]) == b, (l, i, b)
            checked += 1
        quads = [(i, j, k, ll) for i in range(d) for j in range(d)
                 for k in range(d) for ll in range(d)]
        if len(quads) > sample:
            quads = rng.sample(quads, sample)
        for (i, j, k, ll) in quads:
            lhs = mat_mul(E[(i, j)], E[(k, ll)])
            rhs = E[(i, ll)] if j == k else mat_zero(dim)
            assert mat_eq(lhs, rhs), (l, i, j, k, ll)
            checked += 1
    return {"multiplicities": dict(multiplicity), "identities_checked": checked}


def verify_matrix_units_on_sym(G, reps, table, classes, m, sample=30, seed=7):
    U = symmetric_power_rep(G, m)
    mult = {l: v for l, v in multiplicity_in_sym(table, classes, m).items() if v > 0}
    r = verify_matrix_units(G, reps, U, mult, sample, seed)
    r["m"] = m
    return r


def verify_matrix_units_multiplicity_two(G, reps, table, classes):
    m1, m2 = 2, 10
    mult = {}
    a = multiplicity_in_sym(table, classes, m1)
    b = multiplicity_in_sym(table, classes, m2)
    for l in LABELS:
        tot = a[l] + b[l]
        if tot > 0:
            mult[l] = tot
    U = block_diagonal([symmetric_power_rep(G, m1), symmetric_power_rep(G, m2)])
    r = verify_matrix_units(G, reps, U, mult)
    r["expected_multiplicities"] = mult
    return r


def analyze_galois_on_sym_powers(table, classes, max_m=13):
    """Verifica esatta per ogni m se Sym^m(2) è Galois-stabile o coniugata."""
    chars = [[ONE] * 9, list(FUNDAMENTAL_CHARACTER)]
    for k in range(2, max_m + 1):
        chars.append([FUNDAMENTAL_CHARACTER[j] * chars[k - 1][j] - chars[k - 2][j] for j in range(9)])

    results = {}
    for m in range(max_m + 1):
        chi_m = chars[m]
        chi_m_gal = tuple(val.gal() for val in chi_m)
        matched_label = None
        for l in LABELS:
            if tuple(table[l]) == chi_m_gal:
                matched_label = l
                break
        results[m] = {
            "is_stable": (chi_m_gal == tuple(chi_m)),
            "matched_irrep": matched_label
        }
    return results


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
    return poly_mul([ONE] + [ZERO] * 11 + [Num(-1)], [ONE] + [ZERO] * 19 + [Num(-1)])


def class_quotients():
    D = molien_denominator()
    out = []
    for chi in FUNDAMENTAL_CHARACTER:
        quo, rem = poly_div_monic(D, [ONE, -chi, ONE])
        assert rem == [], "resto non nullo"
        out.append(quo)
    return out


def numerator_from_characters(table, label):
    quos = class_quotients()
    acc = []
    for j in range(9):
        w = table[label][j].cconj().scale(Fraction(CLASS_SIZES[j], 120))
        acc = poly_add(acc, [c * w for c in quos[j]])
    return poly_trim(acc)


def numerator_from_t032(label):
    support = IRREP_NUMERATORS[label]
    coeffs = [ZERO] * (max(support) + 1)
    for e in support:
        coeffs[e] = coeffs[e] + ONE
    return poly_trim(coeffs)


def verify_molien_exact(table):
    for l in LABELS:
        mine = numerator_from_characters(table, l)
        theirs = numerator_from_t032(l)
        assert len(mine) == len(theirs) and all(x == y for x, y in zip(mine, theirs)), l
    return {"numerators_checked": 9}


def verify_peter_weyl(max_degree=60):
    for m in range(max_degree + 1):
        total = sum(IRREP_DIMENSIONS[l] * molien_coefficients(l, m)[m] for l in LABELS)
        if total != m + 1:
            return False
    return True


def q5_str(x):
    assert x.is_real()
    if x.b == 0:
        return str(x.a)
    if x.a == 0:
        return f"({x.b})*sqrt5"
    return f"{x.a}+({x.b})*sqrt5"


def export_json(G, reps, table, classes, report):
    minus_idx = G.minus_one
    return {
        "group": "binary_icosahedral_group_2I",
        "order": 120,
        "irreps": {
            l: {
                "dimension": reps[l].dim,
                "construction": reps[l].construction,
                "minus_one_acts_as": ("+I" if reps[l].matrices[minus_idx] == mat_eye(reps[l].dim) else "-I"),
                "values": [x.encode() for x in table[l]],
                "values_text": [q5_str(x) for x in table[l]],
                "generator_s": mat_encode(reps[l].matrices[G.gen_s]),
                "generator_t": mat_encode(reps[l].matrices[G.gen_t]),
            }
            for l in LABELS
        },
        "verification": report,
    }


def run_all(molien_sym_max=13):
    G = build_group()
    report = {"group": verify_group(G)}
    reps = build_representations(G)
    report["homomorphism"] = {l: verify_homomorphism(G, reps[l].matrices) for l in LABELS}
    report["homomorphism_sensitivity"] = verify_homomorphism_detects_error(G, reps["2"].matrices)
    report["weighted_unitarity"] = {l: verify_weighted_unitarity(reps[l]) for l in LABELS if reps[l].weights}
    assert all(report["weighted_unitarity"].values())
    report["galois"] = galois_compatibility(G, reps)
    classes = ordered_classes(G)
    table = mat_trace_class({l: reps[l] for l in LABELS}, G, classes)
    report["character_table"] = verify_character_table(table)
    report["molien_all_degrees"] = verify_molien_exact(table)
    report["multiplicities_vs_molien"] = verify_multiplicities_vs_molien(table, classes, 60)
    report["peter_weyl_sum"] = verify_peter_weyl()
    assert report["peter_weyl_sum"]
    report["schur_entries"] = verify_schur_orthogonality(G, reps)
    report["projectors_on_sym"] = [
        verify_projectors_on_sym(G, table, classes, m, full_orthogonality=(m <= 7))
        for m in range(molien_sym_max + 1)]
    mu = [verify_matrix_units_on_sym(G, reps, table, classes, m) for m in range(8)]
    mu.append(verify_matrix_units_multiplicity_two(G, reps, table, classes))
    report["matrix_units"] = mu
    report["galois_sym_analysis"] = analyze_galois_on_sym_powers(table, classes, molien_sym_max)
    return G, reps, table, classes, report


def main():
    parser = argparse.ArgumentParser(description="T034 Kaggle Verification Suite")
    parser.add_argument("--output", default="/kaggle/working/t034_2i_character_table.json")
    args, _ = parser.parse_known_args()

    print("Esecuzione della suite T034 su Kaggle...")
    G, reps, table, classes, report = run_all()
    
    out_data = export_json(G, reps, table, classes, report)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out_data, indent=2))
    print(f"Verifiche completate con successo! Risultati salvati in: {out_path}")


if __name__ == "__main__":
    main()

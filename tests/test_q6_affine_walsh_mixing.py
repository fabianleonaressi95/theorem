import itertools
from affine_walsh_mixing import profile, exact_norm_profile, direct_commutator_frobenius_squared, run_audit

def test_all_720_coordinate_permutations_partition_into_51_profiles():
    report=run_audit()
    assert report["enumeration"]["coordinate_permutations_enumerated"]==720
    assert report["enumeration"]["distinct_intersection_profiles"]==51
    assert report["enumeration"]["sum_class_multiplicities"]==720

def test_translations_preserve_every_level():
    identity=tuple(range(6))
    for b in [(0,)*6,(1,)*6,(1,0,1,0,1,0)]:
        for j in range(7):
            assert direct_commutator_frobenius_squared(identity,b,j)==0

def test_coordinate_swap_has_exact_selective_profile():
    swap=(0,1,4,3,2,5)
    r=profile(swap)
    assert r==(0,1,2,2,3,5,6)
    norms=exact_norm_profile(r)
    assert norms["frobenius_squared"]==[0,0,0,8,16,0,0]
    assert norms["spectral"]==[0,0,0,1,1,0,0]
    assert abs(norms["frobenius"][3]-2*(2**0.5))<1e-12
    assert norms["frobenius"][4]==4.0

def test_formula_matches_direct_position_basis_commutator():
    swap=(0,1,4,3,2,5)
    norms=exact_norm_profile(profile(swap))
    for j in range(7):
        for b in [(0,)*6,(1,)*6]:
            assert direct_commutator_frobenius_squared(swap,b,j)==norms["frobenius_squared"][j]

def test_identity_linear_part_is_only_one_preserving_all_prefixes():
    for p in itertools.permutations(range(6)):
        if all(profile(p)[j]==j for j in range(7)):
            assert p==tuple(range(6))

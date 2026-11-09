from decimal import Decimal
from fractions import Fraction
import pytest
from models.prism_billiard_coding import (
    continued_fraction_convergents, cycle_lift, hamming_transition_counts,
    q6_six_bit_blocks, return_times, rotation_code, subword_complexity, symbol_frequency,
)

def test_rational_rotation_code_is_exact_and_periodic():
    assert rotation_code(Fraction(2,5),20) == (0,0,1,0,1)*4

def test_decimal_sqrt2_minus_one_initial_symbols():
    alpha=Decimal("0.414213562373095048801688724210")
    assert rotation_code(alpha,8) == (0,0,1,0,1,0,0,1)

def test_convergents_exact():
    assert continued_fraction_convergents([0,2,2,2,2]) == (
        Fraction(0,1),Fraction(1,2),Fraction(2,5),Fraction(5,12),Fraction(12,29))

def test_complexity_and_return_times():
    word=(0,1,0,1,0,1)
    assert subword_complexity(word,2)==2
    assert return_times(word,1)==(2,2)

def test_q6_block_labels_and_hamming():
    labels=q6_six_bit_blocks((1,0,1,0,1,0,1,1,1,0,0,0))
    assert labels==(42,56)
    assert hamming_transition_counts(labels)==(2,)

def test_cycle_lift_and_frequency():
    assert cycle_lift((0,1,1),7)==(0,1,1,0,1,1,0)
    assert symbol_frequency((0,1,1,0))==0.5
    with pytest.raises(ValueError):
        cycle_lift((),4)

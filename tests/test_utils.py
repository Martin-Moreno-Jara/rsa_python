import pytest
from utils.math_utils import mcd, extended_mcd,mod_inverse

@pytest.mark.parametrize(
        "input_a, input_b, expected",
        [
            (5,17,1),
            (11,17,1),
            (15489,1557,9),
            (5568,4478,2),
            (10,15,5),
            (-4,8,4)
        ]
)
def test_mcd_params(input_a,input_b,expected):
    assert mcd(input_a,input_b) == expected

@pytest.mark.parametrize(
        "input_a, input_b, expected_x, expected_y, expected_mcd",
        [
            (15668,66987,10898,-2549, 1),
            (554489, 33645,-14776,243517,1),
            (150, 504,37,-11,6)
        ]
)
def test_extended_mcd_params(input_a,input_b,expected_x,expected_y,expected_mcd):
    assert extended_mcd(input_a,input_b) == (expected_x,expected_y,expected_mcd)

@pytest.mark.parametrize(
        "input_e, input_phi, expected",
        [
            (3,26,9),
            (5669,2254,895),
            (11,25,16),
            (11045,4558,3705)
        ]
)
def test_inverse_mod_params(input_e,input_phi,expected):
    assert mod_inverse(input_e,input_phi) == expected
import pytest
from utils.math_utils import mcd

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

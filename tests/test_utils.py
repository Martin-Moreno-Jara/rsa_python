import pytest
from utils.math_utils import mcd, extended_mcd,mod_inverse,min_divisor,is_prime, mod_exp,generate_prime

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

@pytest.mark.parametrize(
        "input_m, expected",
        [
           (5,5),
           (10,2),
           (15,3),
           (7,7),
           (11,11),
           (17,17),
           (21,3),
           (31,31)
        ]
)
def test_min_divisor_params(input_m,expected):
    assert min_divisor(input_m) == expected

@pytest.mark.parametrize(
        "input_number, expected",
        [
           (5,True),
           (10,False),
           (15,False),
           (7,True),
           (11,True),
           (17,True),
           (31,True),
           (7841,True)
        ]
)
def test_is_prime_params(input_number,expected):
    assert is_prime(input_number) == expected


@pytest.mark.parametrize(
        "input_base, input_exp, input_mod, expected",
        [
            (314159265358,2718281828,123456789,32073907),
            (3,618970019642690137449562110,618970019642690137449562111,1),
            (51688453554555,5655568848565,4458664214,3763127797),
            (17544886699,44114114,2556,2401),
            (175448866998774,441141144452856,2556554487856,869407387968)
        ]
)
def test_mod_exp_params(input_base,input_exp,input_mod,expected):
    assert mod_exp(input_base,input_exp,input_mod) == expected

@pytest.mark.parametrize(
        "input_keysize",
        [
            (4),
            (42),
            (30),
            (25),
            (40),
        ]
)
def test_generate_primes_params(input_keysize):
    assert is_prime(generate_prime(input_keysize))
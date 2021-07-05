import pytest

from hometask.calculator.calculator import Calculator
calc = Calculator()

non_valid_data = [
    (2, "abs", TypeError),
    ("1", 9, TypeError),
]


@pytest.mark.parametrize(
    'x, y, res',
    [
        (2, -2, 0),
        (24, 9, 33),
    ]
)
def test_add_valid_numbers(x, y, res):
    assert calc.add(x, y) == res


@pytest.mark.parametrize(
    'x, y, res',
    non_valid_data
)
def test_add_non_valid_numbers(x, y, res):
    with pytest.raises(res):
        calc.add(x, y)


@pytest.mark.parametrize(
    'x, y, res',
    [
        (2, -2, 4),
        (24, 9, 15),
    ]
)
def test_subtract_valid_numbers(x, y, res):
    assert calc.subtract(x, y) == res


@pytest.mark.parametrize(
    'x, y, res',
    non_valid_data
)
def test_subtract_non_valid_numbers(x, y, res):
    with pytest.raises(res):
        calc.subtract(x, y)


@pytest.mark.parametrize(
    'x, y, res',
    [
        (2, 2, 1),
        (24, 3, 8),
    ]
)
def test_divide_valid_numbers(x, y, res):
    assert calc.divide(x, y) == res


@pytest.mark.parametrize(
    'x, y, res',
    [
        (2, "abs", TypeError),
        ("1", 9, TypeError),
        (2, 0, ValueError)
    ]
)
def test_divide_non_valid_numbers(x, y, res):
    with pytest.raises(res):
        calc.divide(x, y)


@pytest.mark.parametrize(
    'x, y, res',
    [
        (2, 5, 10),
        (1, 0, 0),
    ]
)
def test_multiply_valid_numbers(x, y, res):
    assert calc.multiply(x, y) == res


@pytest.mark.parametrize(
    'x, y, res',
    non_valid_data
)
def test_multiply_non_valid_numbers(x, y, res):
    with pytest.raises(res):
        calc.multiply(x, y)


@pytest.mark.parametrize(
    'x, y, res',
    [
        (5, 2, 1),
        (15, 4, 3)
    ]
)
def test_mod_valid_numbers(x, y, res):
    assert calc.mod(x, y) == res


@pytest.mark.parametrize(
    'x, y, res',
    non_valid_data
)
def test_mod_non_valid_numbers(x, y, res):
    with pytest.raises(res):
        calc.mod(x, y)


@pytest.mark.parametrize(
    'x, y, res',
    [
        (2, 3, 8),
        (15, 2, 225)
    ]
)
def test_power_valid_numbers(x, y, res):
    assert calc.power(x, y) == res


@pytest.mark.parametrize(
    'x, y, res',
    non_valid_data
)
def test_power_non_valid_numbers(x, y, res):
    with pytest.raises(res):
        calc.power(x, y)


@pytest.mark.parametrize(
    'x, res',
    [
        (9, 3),
        (4, 2)
    ]
)
def test_root_valid_numbers(x, res):
    assert calc.root(x) == res


@pytest.mark.parametrize(
    'x, res',
    [
        (0, ValueError),
        ("abs", TypeError)
    ]
)
def test_root_non_valid_numbers(x, res):
    with pytest.raises(res):
        calc.root(x)

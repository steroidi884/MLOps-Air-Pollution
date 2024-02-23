import pytest
def calculate_area_square(length: int | float) -> int | float:
    """
    Function to calculate the area of a square
    :param length: length of the square
    :return: area of the square
    """
    if not isinstance(length, (int, float)) or length <= 0:
        raise TypeError("Length must be a positive non-zero number")
    return length * length



def test_calculate_area_square():
    assert calculate_area_square(2) == 4
    assert calculate_area_square(2.5) == 6.25


def test_calculate_area_square_negative():
    with pytest.raises(TypeError):
        calculate_area_square(-2)


def test_calculate_area_square_string():
    with pytest.raises(TypeError):
        calculate_area_square("2")


def test_calculate_area_square_list():
    with pytest.raises(TypeError):
        calculate_area_square([2])

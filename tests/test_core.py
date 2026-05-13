from parking_functions.core import *
import pytest


def test_park_out_of_bounds():
    with pytest.raises(ValueError):
        park_a_car([1, 2, 3, 4], 5, 4, 1)


def test_park_parks_in_favorite_spot():
    parking_lot = [1, None, None, 4]
    assert park_a_car(parking_lot, 2, 2, 1) == [1, None, 2, 4]


def test_park_parks_in_reverse_order():
    parking_lot = [1, None, 2, 3]
    assert park_a_car(parking_lot, 4, 2, -1) == [1, 4, 2, 3]


def test_park_do_not_park_in_both_directions():
    parking_lot = [1, 2, 3, 4, 5]
    assert park_a_car(parking_lot, 6, 2, -1) == parking_lot
    assert park_a_car(parking_lot, 6, 2, 1) == parking_lot


def test_park_parks_at_boundary():
    parking_lot = [None, 1, 2, 3, 4]
    assert park_a_car(parking_lot, 5, 4, -1) == [5, 1, 2, 3, 4]
    assert park_a_car([1, 2, 3, 4, None], 5, 0, 1) == [1, 2, 3, 4, 5]


def test_parking_parks_all():

    assert parking(10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1] * 10) == list(range(10))
    assert parking(10, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [1] * 10) == list(
        range(9, -1, -1)
    )


def test_parking_might_not_park_all():
    park_result = parking(5, [4, 4, 4, 4, 4], [1] * 5)
    assert park_result == [None, None, None, None, 1]
    assert not all(park_result)

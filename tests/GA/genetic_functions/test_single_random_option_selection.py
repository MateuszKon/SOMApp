import pytest

from GA.genetic_functions.random_option_selection import select_single_different_option


def test_select_single_different_option_single_list():
    list_ = [3]
    current_value = 3
    new_value = select_single_different_option(list_, current_value)
    assert current_value == new_value


def test_select_single_different_option_list():
    list_ = [3, 4]
    current_value = 3
    new_value = select_single_different_option(list_, current_value)
    assert current_value != new_value
    assert new_value in list_



def test_select_single_different_option_empty_list():
    list_ = []
    current_value = 3
    with pytest.raises(AssertionError):
        select_single_different_option(list_, current_value)


def test_select_single_different_option_no_current_value():
    list_ = [1, 2, 3, 4]
    new_value = select_single_different_option(list_)
    assert new_value in list_


def test_select_single_different_option_possible_none():
    list_ = [1, None]
    current_value = 1
    new_value = select_single_different_option(list_, current_value)
    assert new_value is None

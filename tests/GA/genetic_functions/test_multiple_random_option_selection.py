import pytest

from GA.genetic_functions.random_option_selection import \
    factory_select_multiple_options_with_probability


def test_single_element_option_the_same():
    func_ = factory_select_multiple_options_with_probability(2, 1)
    list_ = [3]
    current_value = [3, 3]
    new_value = func_(list_, current_value)
    assert current_value == new_value


def test_always_change_option():
    func_ = factory_select_multiple_options_with_probability(2, 1)
    list_ = [1, 2, 3]
    current_value = [1, 1]
    new_value = func_(list_, current_value)
    assert current_value != new_value

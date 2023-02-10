from pytest_mock import mocker

from GA.gene import Gene

import pytest

from GA.genetic_functions.random_option_selection import \
    factory_select_multiple_options_with_probability


OPTIONS = range(1, 10)
OPTION_NUMBER = 2
PROBABILITY = 0.8


@pytest.fixture()
def multiple_value_gene():
    gene = Gene(
        'dimmensions',
        OPTIONS,
        funct_select_random_option=factory_select_multiple_options_with_probability(OPTION_NUMBER,
                                                                                    PROBABILITY),
    )
    yield gene


def test_generating_value_if_current_none(multiple_value_gene):
    new_value = multiple_value_gene.select_random_value()
    assert len(new_value) == OPTION_NUMBER
    print(new_value)
    for value in new_value:
        assert value in OPTIONS


def test_change_by_probability(multiple_value_gene, mocker):
    old_value = multiple_value_gene.select_random_value()
    mocker.patch('GA.genetic_functions.random_option_selection.random', side_effect=[0.6, 0.9])
    new_value = multiple_value_gene.select_random_value()
    assert old_value[0] != new_value[0]
    assert old_value[1] == new_value[1]

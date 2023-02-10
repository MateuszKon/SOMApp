from random import sample, random
from typing import TypeVar, Sequence, Callable

T = TypeVar('T')
T_V = Sequence[T]


def select_single_different_option(options: Sequence[T], current_value: T = None) -> T:
    assert len(options) > 0
    if len(options) == 1:
        return options[0]
    new_sample, alternative_sample = sample(options, 2)
    return new_sample if new_sample != current_value else alternative_sample


def factory_select_multiple_options_with_probability(option_number: int, probability: float) -> \
        Callable[[Sequence[T], T_V], T_V]:
    def select_multiple_options(options: Sequence[T], current_value: T_V = None) -> T_V:
        if current_value is None:
            current_value = [None for _ in range(option_number)]

        new_value = []
        for i in range(option_number):
            if probability > random() or current_value[i] is None:
                new_value.append(select_single_different_option(options, current_value[i]))
            else:
                new_value.append(current_value[i])
        return new_value

    return select_multiple_options

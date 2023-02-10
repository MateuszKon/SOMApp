from typing import TypeVar, Sequence, Callable, Union

from nptyping import NDArray, Shape, Float

from GA.genetic_functions.random_option_selection import select_single_different_option as \
    default_selection

T = TypeVar('T')
T_V = Union[T, Sequence[T]]


class Gene:

    def __init__(
            self,
            name: str,
            options: Sequence[T],
            current_value: T_V = None,
            funct_select_random_option: Callable[[Sequence[T], T_V], T_V] = default_selection,
            randomize=False,
    ) -> None:
        self.name = name
        self.options = options
        self._value = current_value
        self.funct_select_random_option = funct_select_random_option
        if randomize:
            self.select_random_value()

    def __repr__(self) -> str:
        return f"{self.__class__}({self.name}, {self.value})"

    def __eq__(self, other):
        return other and self.name == other.name and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.name, self.value))

    def select_random_value(self) -> T_V:
        self.value = self.funct_select_random_option(self.options, self.value)
        return self.value

    @property
    def value(self) -> T_V:
        return self._value

    @value.setter
    def value(self, value: T_V) -> None:
        self._value = value


class PropertyGene(Gene):
    pass


class DataGene(Gene):

    def __init__(
            self,
            name: str,
            options: Sequence[T],
            funct_generate_som_data: Callable[[T_V], NDArray[Shape["2, N"], Float]],
            current_value: T_V = None,
            funct_select_random_option: Callable[[Sequence[T], T_V], T_V] = default_selection,
    ) -> None:
        super().__init__(name, options, current_value, funct_select_random_option)
        self.funct_generate_som_data = funct_generate_som_data

    @property
    def data(self) -> NDArray[Shape["2, N"], Float]:
        return self.funct_generate_som_data(self)

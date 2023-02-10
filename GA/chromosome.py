from collections import namedtuple
from typing import Iterator

from GA.gene import DataGene


class Chromosome(namedtuple('Chromosome',
                            [
                                'som_dimensions',
                                'som_iterations_no',
                                'som_learning_rate',
                            ],
                            )):
    __slots__ = ()

    @property
    def data_genes(self) -> Iterator[DataGene]:
        for item in self:
            if isinstance(item, DataGene):
                yield item

    def __repr__(self):
        gens_repr = ", ".join([str(item) for item in self])
        return f"Chromosome({gens_repr})"

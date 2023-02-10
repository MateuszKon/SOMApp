from copy import copy
from typing import Callable, List

import numpy
from pygad import GA

from GA.chromosome import Chromosome
from GA.gene import Gene, PropertyGene


class MyGA(GA):

    supported_int_float_types = GA.supported_int_float_types + [Gene]

    # def __init__(
    #         self,
    #         num_generations: int,
    #         num_parents_mating: int,
    #         fitness_func: Callable,
    #         *args,
    #         **kwargs,
    # ):
    #     super().__init__(
    #         num_generations,
    #         num_parents_mating,
    #         fitness_func,
    #         *args,
    #         **kwargs
    #     )

    def mutation_probs_randomly(self, offspring):
        # Random mutation changes one or more gene in each offspring randomly.
        for offspring_idx in range(offspring.shape[0]):
            probs = numpy.random.random(size=offspring.shape[1])
            for gene_idx in range(offspring.shape[1]):
                if probs[gene_idx] <= self.mutation_probability:
                    offspring[offspring_idx, gene_idx] = copy(offspring[offspring_idx, gene_idx])
                    offspring[offspring_idx, gene_idx].select_random_value()

                    if not self.allow_duplicate_genes:
                        offspring[offspring_idx], _, _ = self.solve_duplicate_genes_randomly(
                            solution=offspring[offspring_idx],
                            min_val=self.random_mutation_min_val,
                            max_val=self.random_mutation_max_val,
                            mutation_by_replacement=self.mutation_by_replacement,
                            gene_type=self.gene_type,
                            num_trials=10)
        return offspring


def my_on_fitness(ga_instance: MyGA, last_fitness):
    # print(last_fitness)
    pass


def my_on_generation(ga_instance: MyGA):
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
    print("Chromosome = {chromosome}".format(chromosome=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[0]))


def chromosome_template() -> Chromosome:
    options = range(1, 100)
    return Chromosome(
        PropertyGene('som_dimensions', options, randomize=True),
        PropertyGene('som_iterations_no', options, randomize=True),
        PropertyGene('som_learning_rate', options, randomize=True)
    )


def my_fitness_function(solution: List[Gene], solution_index: int) -> float:
    # print(solution)
    fitness = 0
    for gene in solution:
        fitness += gene.value
    return 1.1 if fitness == 100 else 1/(abs(fitness - 100))


if __name__ == '__main__':
    num_generations = 50
    sol_per_pop = 20  # 200
    num_parents_mating = 10  # 100
    fitness_func = my_fitness_function

    initial_population = numpy.array(
        [list(chromosome_template()) for _ in range(sol_per_pop)],
        dtype=Gene,
        ndmin=2,
    )

    my_ga = MyGA(
        num_generations,
        num_parents_mating,
        fitness_func,
        initial_population=initial_population,
        sol_per_pop=sol_per_pop,  # 200
        gene_type=Gene,
        parent_selection_type="rws",  # roulette_wheel_selection
        keep_elitism=1,
        crossover_type="uniform",  # uniform_crossover
        crossover_probability=0.1,
        mutation_type="random",  # random_mutation
        mutation_probability=0.8,
        mutation_by_replacement=True,
        save_best_solutions=True,
        on_fitness=my_on_fitness,
        on_generation=my_on_generation,
        parallel_processing=1,
    )

    my_ga.run()

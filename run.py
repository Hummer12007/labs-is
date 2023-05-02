from data import Data
from genetic_algorithm import GeneticAlgorithm, Population
from constants import *

def run():
    i = 0
    data = Data()
    _genetic_algorithm = GeneticAlgorithm(data=data)
    _population = Population(size=POPULATION_SIZE, data=data).sort_by_fitness()

    while _population.schedules[0].fitness != 1.0:
        i += 1
        print('Generation', i)
        _population = _genetic_algorithm.evolve(population=_population).sort_by_fitness()

        for p in _population.schedules:
            print(p, p.fitness, p.number_of_conflicts)

    print('\n\nSolution:\n\n', _population.schedules[0], _population.schedules[0].number_of_conflicts)

if __name__ == '__main__':
    run()

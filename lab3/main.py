import random as rnd

from data import Data
from display import Display
from schedule import Schedule

# Number of schedules in each generation
POPULATION_SIZE = 15
# Number of schedules to be selected for crossover
NUMB_OF_SCHEDULES = 1
# Number of Selected Schedules evey Generation
SELECTION_SIZE = 6
# The chance that a schedule will mutate
MUTATION_RATE = 0.1


class Population:
    def __init__(self, size, data):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0, size):
            self._schedules.append(Schedule(data).initialize())

    def get_schedules(self): return self._schedules


class GeneticAlgorithmScheduler:
    def evolve(self, population):
        return self._mutate(self._crossover(population))

    def _crossover(self, pop):
        crossover_pop = Population(0, data)
        for i in range(NUMB_OF_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_SCHEDULES
        while i < POPULATION_SIZE:
            # Select two schedules for crossover
            schedule1 = self._select_population(pop).get_schedules()[0]
            schedule2 = self._select_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def _mutate(self, population):
        for i in range(NUMB_OF_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule(data).initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            # It randomly selects a class from one of the two schedules
            if (rnd.random() > 0.5):
                crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule

    def _mutate_schedule(self, mutateSchedule):
        # A random schedule, needed as a soruce of random classes
        schedule = Schedule(data).initialize()
        for i in range(0, len(mutateSchedule.get_classes())):
            # With a chance of MUTATION_RATE, it replaces a class with a random class
            if (MUTATION_RATE > rnd.random()): mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule

    # Selects SELECTION_SIZE random schedules and sorts them by fitness
    def _select_population(self, pop):
        tournament_pop = Population(0, data)
        i = 0
        while i < SELECTION_SIZE:
            # Append a random schedule to the tournament population
            tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        # Sort by fitness
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True) 
        return tournament_pop


def print_result(data):
    final_schedule = data

    result = {}
    for i in range(0, len(final_schedule)):
        grade = final_schedule[i].get_course().get_grade()
        if grade not in result:
            result[grade] = []
        result[grade].append(final_schedule[i])

    for key in result:
        print(key + ' group schedule:')
        display.print_classes(result[key])


data = Data()
display = Display(data)
generationNumber = 0

population = Population(POPULATION_SIZE, data)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)

display.print_schedule(population.get_schedules()[0])

geneticAlgorithm = GeneticAlgorithmScheduler()

while population.get_schedules()[0].get_fitness() != 1.0:
    generationNumber += 1

    print("\n--- Generation # " + str(generationNumber) + ". Fitness: "
          + str(population.get_schedules()[0].get_fitness()))

    # Propagate new generation
    population = geneticAlgorithm.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)

print("\n--- Final Generation # " + str(generationNumber) + ". Fitness: "
      + str(population.get_schedules()[0].get_fitness()) + "\n\n")

final_schedule = population.get_schedules()[0].get_classes()
print_result(final_schedule)

print("\n\n")

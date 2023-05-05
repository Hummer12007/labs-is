import random


POPULATION_SIZE = 100
MUTATION_RATE = 0.1
GENERATIONS = 100


CLASSES = ['Math', 'English', 'Physics', 'Chemistry', 'History', 'Geography']
TEACHERS = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis']
STUDENTS = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank']


def generate_initial_population(population_size):
    population = []
    for i in range(population_size):
        schedule = []
        for j in range(len(CLASSES)):
            time = random.randint(1, 5)
            teacher = random.choice(TEACHERS)
            students = random.sample(STUDENTS, random.randint(1, 6))
            schedule.append((time, CLASSES[j], teacher, students))
        population.append(schedule)
    return population


def calculate_fitness(schedule):
    conflicts = 0
    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):
            if schedule[i][0] == schedule[j][0]:
                if schedule[i][2] == schedule[j][2]:
                    conflicts += 1
                for student in schedule[i][3]:
                    if student in schedule[j][3]:
                        conflicts += 1
    return 1 / (conflicts + 1)


def mutate(schedule):
    for i in range(len(schedule)):
        if random.random() < MUTATION_RATE:
            schedule[i] = (random.randint(1, 5), schedule[i][1], random.choice(TEACHERS), random.sample(STUDENTS, random.randint(1, 6)))
    return schedule


def crossover(schedule1, schedule2):
    crossover_point = random.randint(1, len(CLASSES) - 1)
    return schedule1[:crossover_point] + schedule2[crossover_point:], schedule2[:crossover_point] + schedule1[crossover_point:]


def select_best(population, fitness_scores):
    best = None
    best_score = 0
    for i in range(len(population)):
        if fitness_scores[i] > best_score:
            best = population[i]
            best_score = fitness_scores[i]
    return best


def solve_schedule():
    population = generate_initial_population(POPULATION_SIZE)
    for _ in range(GENERATIONS):
        fitness_scores = [calculate_fitness(schedule) for schedule in population]
        best_schedule = select_best(population, fitness_scores)
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1 = random.choices(population, weights=fitness_scores)[0]
            parent2 = random.choices(population, weights=fitness_scores)[0]
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.append(child1)
            new_population.append(child2)
        population = new_population
    return best_schedule


if __name__ == '__main__':
    best_schedule = solve_schedule()
    print(f'Best schedule: {best_schedule}')
    print(f'Fitness score: {calculate_fitness(best_schedule)}')
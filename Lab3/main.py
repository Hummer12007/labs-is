import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def fitness_function(x):
    return x**2

def create_population(size):
    return np.random.uniform(low=-10, high=10, size=size)

def tournament_selection(population, fitness, k):
    selected = np.random.choice(population.shape[0], k, replace=False)
    best = selected[np.argmax(fitness[selected])]
    return population[best]

def crossover(parents):
    return (parents[0] + parents[1])/2

def mutation(offspring):
    return offspring + np.random.uniform(-1, 1)

def run_genetic_algorithm(population_size, num_generations, k=3, elitism=0.1):
    best_solutions = []
    population = create_population(population_size)
    for generation in range(num_generations):
        fitness = fitness_function(population)
        best_solution = np.max(fitness)
        best_solutions.append(best_solution)
        new_population = []
        num_elites = int(elitism * population_size)
        elites = population[np.argsort(fitness)[-num_elites:]]
        new_population.extend(elites)
        for i in range(population_size - num_elites):
            parents = [tournament_selection(population, fitness, k) for _ in range(2)]
            offspring_crossover = crossover(parents)
            offspring_mutation = mutation(offspring_crossover)
            new_population.append(offspring_mutation)
        population = np.array(new_population)
    return best_solutions

population_size = 100
num_generations = 500
best_solutions = run_genetic_algorithm(population_size, num_generations)

plt.subplot(1, 2, 1)
plt.plot(best_solutions)
plt.title("Genetic Algorithm Visualization")
plt.xlabel("Generation")
plt.ylabel("Best Solution")

G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4)])
pos = nx.spring_layout(G)
nx.draw(G, pos)
labels = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
nx.draw_networkx_labels(G, pos, labels)

plt.subplot(1, 2, 2)
plt.title("Graph Visualization")
plt.axis('off')

plt.show()
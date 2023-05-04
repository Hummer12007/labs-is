import random
import networkx as nx
import matplotlib.pyplot as plt

num_nodes = 100
num_edges = 110

G = nx.gnm_random_graph(num_nodes, num_edges)
pos = nx.spring_layout(G)

population_size = 50
num_generations = 1000
crossover_rate = 0.8
mutation_rate = 0.1
tournament_size = 3


def fitness(individual, graph):
    independent_set_size = 0

    for i in range(len(individual)):
        if individual[i] == 1:
            is_independent = True
            for j in range(i + 1, len(individual)):
                if individual[j] == 1 and graph.has_edge(i, j):
                    is_independent = False
                    break
            if is_independent:
                independent_set_size += 1

    return independent_set_size



def tournament_selection(population, fitness_values, k):
    selected_indices = random.sample(range(len(population)), k)
    best_index = max(selected_indices, key=lambda i: fitness_values[i])
    return population[best_index]


def single_point_crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2


def mutate(individual, mutation_rate):
    return [gene if random.random() > mutation_rate else 1 - gene for gene in individual]


def visualize_graph(graph, best_solution):
    pos = nx.kamada_kawai_layout(graph)
    node_colors = ['red' if best_solution[i] == 1 else 'blue' for i in range(len(best_solution))]
    nx.draw(graph, pos, with_labels=True, node_color=node_colors, node_size=800, font_weight='bold', font_color='white')
    plt.show()

population = [[random.choice([0, 1]) for _ in range(len(G.nodes))] for _ in range(population_size)]

best_solution = max(population, key=lambda ind: fitness(ind, G))
best_fitness = fitness(best_solution, G)

for generation in range(num_generations):
    new_population = []

    for _ in range(population_size // 2):
        parent1 = tournament_selection(population, [fitness(ind, G) for ind in population], tournament_size)
        parent2 = tournament_selection(population, [fitness(ind, G) for ind in population], tournament_size)

        if random.random() < crossover_rate:
            offspring1, offspring2 = single_point_crossover(parent1, parent2)
        else:
            offspring1, offspring2 = parent1, parent2

        offspring1 = mutate(offspring1, mutation_rate)
        offspring2 = mutate(offspring2, mutation_rate)

        new_population.extend([offspring1, offspring2])

    population = new_population

    current_best_solution = max(population, key=lambda ind: fitness(ind, G))
    current_best_fitness = fitness(current_best_solution, G)

    if current_best_fitness > best_fitness:
        best_solution = current_best_solution
        best_fitness = current_best_fitness
        visualize_graph(G, best_solution)
    print(generation, current_best_fitness)

visualize_graph(G, best_solution)
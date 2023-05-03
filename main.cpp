#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include "Solution.h"
#include "Knapsack.h"

// Genetic params
const int POPULATION_SIZE = 100;
const int NUM_GENERATIONS = 1000;

std::vector<Solution> initializePopulation(int popSize, Knapsack* knapsack) {
    Solution::setKnapsack(knapsack);
    std::vector<Solution> population;
    for (int i = 0; i < popSize; i++) {
        population.push_back(Solution());
    }
    return population;
}

std::pair<Solution, Solution> selectParents(const std::vector<Solution>& population) {
    // Create a distribution for selecting parents with a bias towards higher fitness
    std::vector<double> fitnesses(population.size());
    double totalFitness = 0.0;
    for (int i = 0; i < population.size(); i++) {
        totalFitness += population[i].getFitness();
        fitnesses[i] = totalFitness;
    }
    std::default_random_engine generator;
    std::uniform_real_distribution<double> d_distribution(0.0, totalFitness);

    // More fit parents are linearly more likely to be chosen.
    Solution parent1;
    Solution parent2;
    for (int i = 0; i < 2; i++) {
        double value = d_distribution(generator);
        int j = 0;
        while (fitnesses[j] < value) {
            j++;
        }
        parent1 = population[j];
        value = d_distribution(generator);
        j = 0;
        while (fitnesses[j] < value) {
            j++;
        }
        parent2 = population[j];
    }
    return std::make_pair(parent1, parent2);
}

std::vector<Solution> evolvePopulation(const std::vector<Solution>& population) {
    std::vector<Solution> newPopulation(population.size());
    for (int i = 0; i < population.size(); i++) {
        // Select parents
        std::pair<Solution, Solution> parents = selectParents(population);
        // Perform crossover
        Solution child = Solution(parents.first, parents.second);
        // Perform mutation
        child.mutate();
        // Add child to new population
        newPopulation[i] = child;
    }
    // Sort the new population by fitness
    std::sort(newPopulation.begin(), newPopulation.end());
    return newPopulation;
}

Solution solveKnapsack(Knapsack* knapsack) {
    // Initialize the random number generator
    std::random_device rd;
    std::mt19937 rand(rd());
    // Initialize the population
    std::vector<Solution> population = initializePopulation(POPULATION_SIZE, knapsack);
    // Evolve the population for a fixed number of generations
    for (int i = 0; i < NUM_GENERATIONS; i++) {
        population = evolvePopulation(population);
    }
    // Return the best solution
    return population[0];
}

// Relatively simple example to ensure the code is working.
//Knapsack knapsack = Knapsack{
//    50, 10,
//    {10, 20, 30, 40, 50, 10, 20, 30, 40, 50},
//    {50, 40, 30, 20, 10, 50, 40, 30, 20, 10}
//};

Knapsack knapsack = Knapsack {
    100, 20, // max_weight; n_items;
    { 31, 26, 72, 17, 48, 55, 69, 77, 58, 12, 15, 98, 48, 56, 44, 24, 51, 95, 98, 29 }, // weights
    {  9, 15, 27,  8, 14, 25, 16, 22, 21, 13, 18, 30, 28, 21, 17, 11, 25, 23, 26, 24 } // values
};
// On this test example, 1000 generations is not enough to arrive at the optimal solution.

int main() {
    Solution solution = solveKnapsack(&knapsack);
    solution.print();
    return 0;
}

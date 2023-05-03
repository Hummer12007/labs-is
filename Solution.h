#include "Knapsack.h"

const double MUTATION_RATE = 0.1;

class Solution {

    std::vector<bool> items;
    int value;
    int weight;
    static Knapsack* knapsack;
    static int knapsack_size;

public:
    static void setKnapsack(Knapsack* knapsack_ref) {
        knapsack = knapsack_ref;
        knapsack_size = knapsack->getNumberItems();
    }

    Solution() {
        items.resize(knapsack_size, false);
        for (int j = 0; j < items.size(); j++) {
            items[j] = (bool)(rand() % 2);
        }
        calculateFitness();
    }

    Solution(const Solution& parent1, const Solution& parent2) { // crossover

        items.resize(knapsack_size, false);

        int splitIndex = rand() % knapsack_size;
        for (int i = 0; i < splitIndex; i++) {
            items[i] = parent1.items[i];
        }
        for (int i = splitIndex; i < knapsack_size; i++) {
            items[i] = parent2.items[i];
        }
        calculateFitness();
    }

    void mutate() {
        for (int i = 0; i < knapsack_size; i++) {
            if ((double)rand() / RAND_MAX < MUTATION_RATE) {
                items[i] = !items[i];
            }
        }
        calculateFitness();
    }

    void calculateFitness() {
        weight = 0;
        value = 0;
        for (int i = 0; i < items.size(); i++) {
            if (items[i]) {
                weight += knapsack->getItemWeight(i);
                value += knapsack->getItemValue(i);
            }
        }
        if (!isValid()) {
            value = 0;
        }
    }

    int getFitness() const {
        return value;
    }

    bool isValid() {
        return (weight <= knapsack->getMaxWeight());
    }

    bool operator < (const Solution& other) const {
        return (value > other.value);
    }

    void print() {
        std::cout << "Items in knapsack: ";
        for (int i = 0; i < knapsack->getNumberItems(); i++) {
            if (this->items[i]) {
                std::cout << i << " (w=" << knapsack->getItemWeight(i) << ", v=" << knapsack->getItemValue(i) << "); ";
            }
        }
        std::cout << std::endl;
        std::cout << "Total value: " << this->value << std::endl;
        std::cout << "Total weight: " << this->weight << std::endl;
    }
};

Knapsack* Solution::knapsack = nullptr;
int Solution::knapsack_size = 0;

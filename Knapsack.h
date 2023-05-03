#ifndef KNAPSACK_H
#define KNAPSACK_H

struct Knapsack {
    const int max_weight;
    const int n_items;
    const int weights[1000];
    const int values[1000];

    int getNumberItems() const {
        return n_items;
    }

    int getMaxWeight() const {
        return max_weight;
    }

    int getItemWeight(int i) const {
        return weights[i];
    }

    int getItemValue(int i) const {
        return values[i];
    }
};

#endif

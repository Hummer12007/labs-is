#ifndef MAPGENERATOR_H
#define MAPGENERATOR_H
#include <array>
#include <functional>
#include <random>
#include "HelperStructs.h"

template<int w, int h>
class MapGenerator
{
public:
    MapGenerator() : width(w), height(h)
    {
    }

    Grid<w,h> generateRandom() {
        Grid<w,h> labyrinth;
        for (int y = 0; y < h; y++) {
            for (int x = 0; x < w; x++) {
                labyrinth[y][x] = bool_coin();
            }
        }
        return labyrinth;
    }

private:
    const int width;
    const int height;

    std::mt19937 generator{std::random_device{}()};
    std::uniform_int_distribution<unsigned> distribution{0,1};
    decltype(bind(std::ref(distribution), std::ref(generator))) bool_coin{
      bind(std::ref(distribution), std::ref(generator))
    };
};

#endif // MAPGENERATOR_H

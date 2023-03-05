#ifndef HELPERSTRUCTS_H
#define HELPERSTRUCTS_H
#include <cstdlib>
#include <cassert>
#include <array>

template<int w, int h>
using Grid = std::array<std::array<bool, w>, h>;

struct Coord {
    int x = 0;
    int y = 0;

    Coord() = default;
    Coord(int x, int y) {
        this->x = x;
        this->y = y;
    }
};

struct Dimensions {
    int w = 0;
    int h = 0;

    Dimensions() = default;

    Dimensions(int w, int h) {
        assert(w > 0);
        assert(h > 0);
        this->w = w;
        this->h = h;
    }
};

#endif // HELPERSTRUCTS_H

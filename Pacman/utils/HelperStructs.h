#ifndef HELPERSTRUCTS_H
#define HELPERSTRUCTS_H
#include <cstdlib>
#include <cassert>
#include <array>


enum class Tile {
    Blank,
    Wall,
    Coin,
    Player,
    Ghost,
    Cherry,
};

enum class Step {
    N,
    E,
    S,
    W,
    None,
};


template<int w, int h>
using Grid = std::array<std::array<Tile, w>, h>;

struct Coord {
    int x = 0;
    int y = 0;

    Coord() = default;
    Coord(int x, int y) {
        this->x = x;
        this->y = y;
    }

    bool operator == (const Coord& b) const {
        return this->x == b.x && this->y == b.y;
    }

    bool operator < (const Coord& b) const {
        if (this->x < b.x) return true;
        if (this->x > b.x) return false;
        return this->y < b.y;
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

#ifndef GAMESTATE_H
#define GAMESTATE_H
#include <array>
#include <vector>
#include "../utils/HelperStructs.h"
#include <random>

template<int w, int h>
class GameState
{
private:
public:
    GameState() : WIDTH(w), HEIGHT(h) {
    }

    void setMap(Grid<w,h> map) {
        grid = map;
    }


    Tile getTile(int x, int y) {
        return grid[y][x];
    }

    Tile getTile(Coord p) {
        return grid[p.y][p.x];
    }

    void setTile(int x, int y, Tile tile) {
        grid[y][x] = tile;
    }

    void setTile(Coord p, Tile tile) {
        grid[p.y][p.x] = tile;
    }

    Coord getRandomTile() {
        std::random_device dev;
        std::mt19937 rng(dev());
        std::uniform_int_distribution<int> rng_y(1,this->HEIGHT);
        std::uniform_int_distribution<int> rng_x(1,this->WIDTH);

        return { rng_x(rng), rng_y(rng) };
    }

    virtual std::vector<Coord> getAvailableNeighbors(Coord pos) = 0;

protected:

    std::vector<Coord> getAllNeighbors(Coord pos) {
        int x = pos.x;
        int y = pos.y;
        std::vector<Coord> neighbors;
        if (x > 0)     { neighbors.push_back(Coord(x - 1, y    )); }
        if (y > 0)     { neighbors.push_back(Coord(x    , y - 1)); }
        if (y < h - 1) { neighbors.push_back(Coord(x    , y + 1)); }
        if (x < w - 1) { neighbors.push_back(Coord(x + 1, y    )); }
        return neighbors;
    }

private:
    const int WIDTH, HEIGHT;
    std::array<std::array<Tile, w>, h> grid;
    const Coord player_position;
    const Coord goal;
};

#endif // GAMESTATE_H

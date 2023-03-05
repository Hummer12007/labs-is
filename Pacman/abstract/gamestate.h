#ifndef GAMESTATE_H
#define GAMESTATE_H
#include <array>
#include <vector>
#include "../utils/HelperStructs.h"

template<int w, int h>
class GameState
{
private:
public:
    GameState() : WIDTH(w), HEIGHT(h){
    }

    void setMap(Grid<w,h> map) {
        walls = map;
    }


    bool isWall(int x, int y) {
        return walls[x][y];
    }

    void getAvailableNeighbors(Coord pos) = 0;

protected:

    std::vector<Coord> getAllNeighbors(Coord pos) {
        int x = pos.x;
        int y = pos.y;
        std::vector<Coord> neighbors;
        if (x > 0 && y > 0)   {neighbors.push_back(Coord(x-1, y-1));}
        if (x > 0)            {neighbors.push_back(Coord(x-1, y));}
        if (x > 0 && y < h-1) {neighbors.push_back(Coord(x-1, y+1));}
        if (y > 0)   {neighbors.push_back(Coord(x, y-1));}
        if (y < h-1) {neighbors.push_back(Coord(x, y+1));}
        if (x < w-1 && y > 0)   {neighbors.push_back(Coord(x+1, y-1));}
        if (x < w-1)            {neighbors.push_back(Coord(x+1, y));}
        if (x < w-1 && y < h-1) {neighbors.push_back(Coord(x+1, y+1));}
        return neighbors;
    }

private:
    const int WIDTH, HEIGHT;
    std::array<std::array<bool, w>, h> walls;
    const Coord player_position;
    const Coord goal;
};

#endif // GAMESTATE_H

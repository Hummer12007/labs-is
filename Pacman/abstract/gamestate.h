#ifndef GAMESTATE_H
#define GAMESTATE_H
#include <array>
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

private:
    const int WIDTH, HEIGHT;
    std::array<std::array<bool, w>, h> walls;
};

#endif // GAMESTATE_H

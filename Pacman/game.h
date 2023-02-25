#ifndef GAME_H
#define GAME_H
#include "labyrinthstate.h"
#include "utils/mapgenerator.h"

class Game
{
private:
    static constexpr unsigned N_GHOSTS = 3;
    static constexpr int WIDTH = 10;
    static constexpr int HEIGHT = 10;

public:
    Game();
    MapGenerator<WIDTH, HEIGHT>* map_generator;
    LabyrinthState<WIDTH, HEIGHT, N_GHOSTS>* labyrinth_state;

    int getWidth() { return WIDTH; }
    int getHeight() { return HEIGHT; }
    unsigned getNGhosts() { return N_GHOSTS; }
    LabyrinthState<WIDTH, HEIGHT, N_GHOSTS>* getState() {return labyrinth_state; }
};

#endif // GAME_H

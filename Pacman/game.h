#ifndef GAME_H
#define GAME_H
#include "labyrinthstate.h"
#include "utils/mapgenerator.h"
#include "pacman.h"

class Game
{
private:
    static constexpr unsigned N_GHOSTS = 3;

public:
    static constexpr int WIDTH = 21;
    static constexpr int HEIGHT = 21;
    Game();
    MapGenerator<WIDTH, HEIGHT>* map_generator;
    LabyrinthState<WIDTH, HEIGHT, N_GHOSTS>* labyrinth_state;
    Pacman<WIDTH, HEIGHT, N_GHOSTS>* pacman;

    int getWidth() { return WIDTH; }
    int getHeight() { return HEIGHT; }
    unsigned getNGhosts() { return N_GHOSTS; }
    LabyrinthState<WIDTH, HEIGHT, N_GHOSTS>* getState() { return labyrinth_state; }
    void step_greedy();
    void step_search();

    void flipTile();
};

#endif // GAME_H

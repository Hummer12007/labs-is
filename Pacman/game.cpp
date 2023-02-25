#include "game.h"

Game::Game()
{
    map_generator = new MapGenerator<WIDTH, HEIGHT>();
    labyrinth_state = new LabyrinthState<WIDTH, HEIGHT, N_GHOSTS>();
    labyrinth_state->setMap(map_generator->generateRandom());
}

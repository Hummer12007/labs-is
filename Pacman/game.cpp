#include "game.h"

Game::Game()
{
    map_generator = new MapGenerator<WIDTH, HEIGHT>();
    labyrinth_state = new LabyrinthState<WIDTH, HEIGHT, N_GHOSTS>();
    labyrinth_state->setMap(map_generator->generateMap(CLASSIC_MAP));
    labyrinth_state->parseStartingMap();
    pacman = new Pacman<WIDTH, HEIGHT, N_GHOSTS>(labyrinth_state);
}

void Game::flipTile() {
    auto now = this->labyrinth_state->getTile(0, 0);
    if (now == Tile::Wall) {
        this->labyrinth_state->setTile(0, 0, Tile::Cherry);
    } else {
        this->labyrinth_state->setTile(0, 0, Tile::Wall);
    }
}

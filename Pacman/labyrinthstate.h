#ifndef LABYRINTHSTATE_H
#define LABYRINTHSTATE_H
#include "utils/HelperStructs.h"
#include "abstract/gamestate.h"
#include <array>


template<int w, int h, int n_ghosts>
class LabyrinthState : public GameState<w, h>
{

public:
    LabyrinthState() : N_GHOSTS(n_ghosts){
    }

    Coord pacman_position;
    std::array<Coord, n_ghosts> ghost_positions;

    std::vector<Coord> getAvailableNeighbors(Coord pos) override {
        std::vector<Coord> neighbors;
        for (auto cell: this->getAllNeighbors(pos)) {
            if (!this->isWall(cell)) {
                neighbors.push_back(cell);
            }
        }
        return neighbors;
    }

private:
    const int N_GHOSTS;

};

#endif // LABYRINTHSTATE_H

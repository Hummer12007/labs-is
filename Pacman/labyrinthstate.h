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

private:
    const int N_GHOSTS;

};

#endif // LABYRINTHSTATE_H

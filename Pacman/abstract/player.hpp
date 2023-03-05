#ifndef PLAYER_HPP
#define PLAYER_HPP
#include "../utils/HelperStructs.h"

class Player {

    Player() {
        position = Coord(0, 0);
    }

    virtual void findPath() = 0;
    virtual void nextStep() = 0;

private:
    Coord position;
};

#endif // PLAYER_HPP

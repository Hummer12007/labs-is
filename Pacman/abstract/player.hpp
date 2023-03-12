#ifndef PLAYER_HPP
#define PLAYER_HPP
#include "../utils/HelperStructs.h"

class Player {
    virtual Step findPath() = 0;
    virtual Step findGreedy() = 0;

public:
    Player() = default;
    virtual void nextStep() = 0;

private:
    Coord position;
};

#endif // PLAYER_HPP

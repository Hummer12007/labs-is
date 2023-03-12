#ifndef LABYRINTHSTATE_H
#define LABYRINTHSTATE_H
#include "utils/HelperStructs.h"
#include "abstract/gamestate.h"
#include <array>
#include <set>
#include <optional>
#include <cassert>


template<int w, int h, int n_ghosts>
class LabyrinthState : public GameState<w, h>
{

public:
    LabyrinthState() : N_GHOSTS(n_ghosts) {
        coins = std::set<Coord>();
    }

    std::array<Coord, n_ghosts> ghost_positions;
    std::set<Coord> coins;


    std::vector<Coord> getAvailableNeighbors(Coord pos) override {
        std::vector<Coord> neighbors;
        for (auto cell: this->getAllNeighbors(pos)) {
            if (this->getTile(cell.x, cell.y) != Tile::Wall) {
                neighbors.push_back(cell);
            }
        }
        return neighbors;
    }

    int num_coins() {
        return this->coins.size();
    }

    bool spawn_coin(std::optional<Coord> pos) {
        if (pos.has_value()) {
            auto p = pos.value();
            if (coins.count(p)) {
                assert (this->getTile(p.x, p.y) == Tile::Coin);
                return false;
            } 
            if (this->getTile(p.x, p.y) != Tile::Blank) {
                return false;
            }
            this->coins.emplace(p);
            this->setTile(p.x, p.y, Tile::Coin);
            return true;
        }
        for (int i = 0; i < 10; ++i) {
            auto p = this->getRandomTile();
            if (coins.count(p)) {
                assert (this->getTile(p.x, p.y) == Tile::Coin);
                continue;
            } 
            if (this->getTile(p.x, p.y) != Tile::Blank) {
                continue;
            }
            this->coins.emplace(p);
            this->setTile(p.x, p.y, Tile::Coin);
            return true;
        }
        return false;
    }

    void take_coin(Coord pos) {
        assert(coins.count(pos));
        coins.erase(pos);
    }

    void parseStartingMap() {
        for (int y = 0; y < h; ++y) {
            for (int x = 0; x < w; ++x) {
                if (this->getTile(x, y) == Tile::Coin) {
                    this->coins.emplace(Coord({x, y}));
                }
            }
        }
    }
    
private:
    const int N_GHOSTS;

};

#endif // LABYRINTHSTATE_H

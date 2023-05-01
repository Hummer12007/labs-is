#include "labyrinthstate.h"
#include "utils/HelperStructs.h"
#include "abstract/player.hpp"
#include <limits>
#include <queue>
#include <tuple>
#include <optional>


template<int w, int h, int n_ghosts>
class Pacman : public Player {
private:
    LabyrinthState<w, h, n_ghosts>* labyrinth_state;
    Coord pos;
    std::optional<Coord> next_goal;

    Step findPath() override {
        if (labyrinth_state->num_coins() == 0) {
            return Step::None;
        }
        typedef std::tuple<int, Coord, Step> q_val;
        std::priority_queue<q_val> pq;
        auto [px, py] = pos;
        pq.push({-1, {px + 1, py}, Step::E});
        pq.push({-1, {px - 1, py}, Step::W});
        pq.push({-1, {px, py + 1}, Step::S});
        pq.push({-1, {px, py - 1}, Step::N});

        std::set<Coord> seen = {pos};

        while (!pq.empty()) {
            auto [steps, tile_pos, dir] = pq.top();
            pq.pop();
            if (seen.count(tile_pos) or labyrinth_state->getTile(tile_pos.x, tile_pos.y) == Tile::Wall) {
                continue;
            }
            seen.emplace(tile_pos);
            if (labyrinth_state->getTile(tile_pos.x, tile_pos.y) == Tile::Coin) {
                return dir;
            }
            pq.push({steps-1, {tile_pos.x + 1, tile_pos.y}, dir});
            pq.push({steps-1, {tile_pos.x - 1, tile_pos.y}, dir});
            pq.push({steps-1, {tile_pos.x, tile_pos.y + 1}, dir});
            pq.push({steps-1, {tile_pos.x, tile_pos.y - 1}, dir});
        }

        return Step::None;
    }

    Step findGreedy() override {
        if (labyrinth_state->num_coins() == 0) {
            return Step::None;
        }
        if (!next_goal.has_value()) {
            Coord closest = *labyrinth_state->coins.begin();
            for (const auto& q : labyrinth_state->coins) {
                if (l1(pos, q) < l1(pos, closest)) {
                    closest = q;
                }
            }
            next_goal = {closest};
        }
        typedef std::tuple<int, Coord, Step> q_val;
        std::priority_queue<q_val> pq;
        auto [px, py] = pos;
        pq.push({-l1({px + 1, py}, next_goal.value()), {px + 1, py}, Step::E});
        pq.push({-l1({px - 1, py}, next_goal.value()), {px - 1, py}, Step::W});
        pq.push({-l1({px, py + 1}, next_goal.value()), {px, py + 1}, Step::S});
        pq.push({-l1({px, py - 1}, next_goal.value()), {px, py - 1}, Step::N});

        std::set<Coord> seen = {pos};
        while (!pq.empty()) {
            auto [dist, tile_pos, dir] = pq.top();
            pq.pop();
            if (seen.count(tile_pos) or labyrinth_state->getTile(tile_pos.x, tile_pos.y) == Tile::Wall) {
                continue;
            }
            seen.emplace(tile_pos);
            if (next_goal.value() == tile_pos) {
                return dir;
            }
            pq.push({-l1({tile_pos.x + 1, tile_pos.y}, next_goal.value()), {tile_pos.x + 1, tile_pos.y}, dir});
            pq.push({-l1({tile_pos.x - 1, tile_pos.y}, next_goal.value()), {tile_pos.x - 1, tile_pos.y}, dir});
            pq.push({-l1({tile_pos.x, tile_pos.y + 1}, next_goal.value()), {tile_pos.x, tile_pos.y + 1}, dir});
            pq.push({-l1({tile_pos.x, tile_pos.y - 1}, next_goal.value()), {tile_pos.x, tile_pos.y - 1}, dir});
        }

        return Step::E;
    }

    int l1(Coord p, Coord q) {
        auto [px, py] = p;
        auto [qx, qy] = q;
        return abs(px - qx) + abs(py - qy);
    }

    Coord stepToCoord(Step dir) {
        switch (dir) {
        case Step::N:
            return { pos.x, pos.y - 1 };
        case Step::E:
            return { pos.x + 1, pos.y };
        case Step::S:
            return { pos.x, pos.y + 1 };
        case Step::W:
            return { pos.x - 1, pos.y };
        case Step::None:
            return { pos.x, pos.y };
        default:
            assert(false);
        }
    }

    void stepOntoTile() {
        if (next_goal.has_value() and pos == next_goal.value()) {
            next_goal = {};
        }
        Tile tile = labyrinth_state->getTile(pos);
        switch (tile) {
        case Tile::Blank:
            return;
        case Tile::Player:
            return;
        case Tile::Coin:
            labyrinth_state->take_coin(pos);
            return;
        case Tile::Wall:
            assert(false);
        case Tile::Ghost:
            assert(false);
        case Tile::Cherry:
            assert(false);
        default:
            assert(false);
        }
    }

public:
    Pacman(LabyrinthState<w, h, n_ghosts>* lab) {
        labyrinth_state = lab;
        next_goal = {};
        int player_count = 0;
        pos = { -1, -1 };
        for (int y = 0; y < h; ++y) {
            for (int x = 0; x < w; ++x) {
                if (this->labyrinth_state->getTile(x, y) == Tile::Player) {
                    pos = { x, y };
                    player_count += 1;
                }
            }
        }
        assert (player_count == 1);
        
        lab->setTile(pos.x, pos.y, Tile::Player);
    }

    void nextStep() override {
        assert (labyrinth_state->getTile(pos) == Tile::Player);
        labyrinth_state->setTile(pos, Tile::Blank);
        auto dir = findPath();
        // auto dir = findGreedy();
        pos = stepToCoord(dir);
        stepOntoTile();
        labyrinth_state->setTile(pos, Tile::Player);
    }

};


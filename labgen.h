#pragma once
#include <vector>

typedef std::pair<int, int> point;
#define x first
#define y second
const std::vector<point> moves = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };

struct Maze
{
    std::vector<std::vector<bool> > left_walls;
    std::vector<std::vector<bool> > upper_walls;
};

Maze GenerateMaze(int n, int m);

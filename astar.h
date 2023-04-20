#pragma once
#include "labgen.h"

std::vector<point> AStar(Maze& maze, point s, point t, std::vector<point>& visited);

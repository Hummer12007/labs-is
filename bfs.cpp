#include "bfs.h"
#include <cmath>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

std::vector<point> BFS(Maze& maze, point s, point t, std::vector<point>& visited)
{
    int n = maze.left_walls.size();
    int m = maze.left_walls[0].size();
    visited.clear();

    set<point> already_visited;
    map<point, int> distance; distance[s] = 0;
    set<pair<int, point> > prior_queue = { {0, s} };
    map<point, point> parent;

    while (true)
    {
        point p = prior_queue.begin()->second;
        prior_queue.erase(prior_queue.begin());
        visited.push_back(p);
        int d = distance[p];
        already_visited.insert(p);

        if (p == t)
        {
            vector<point> res = { p };
            while (p != s)
            {
                p = parent[p];
                res.push_back(p);
            }
            reverse(res.begin(), res.end());
            return res;
        }

        for (point dp : moves)
        {
            point p1 = point{ (p.x + dp.x + n)%n, (p.y + dp.y + m)%m };
            if ((dp == point{-1, 0}) && maze.upper_walls[p.x][p.y]) continue;
            if ((dp == point{0, -1}) && maze.left_walls[p.x][p.y]) continue;
            if ((dp == point{0,  1}) && maze.left_walls[p1.x][p1.y]) continue;
            if ((dp == point{ 1, 0}) && maze.upper_walls[p1.x][p1.y]) continue;

            if (already_visited.count(p1))
                continue;
            if (!distance.count(p1) || distance[p1] > d+1)
            {
                distance[p1]=d+1;
                prior_queue.insert({d+1, p1});
                parent[p1] = p;
            }
        }
    }
}

#include "labgen.h"
#include <random>
#include <iostream>

using namespace std;

Maze GenerateMaze(int n, int m)
{
    Maze maze;
    maze.left_walls = maze.upper_walls = vector<vector<bool> >(n, vector<bool>(m, 1));
    vector<vector<int> > cells(n, vector<int>(m, 0));
    cells[0][0] = 1;
    for (int i=0; i<n; i++)
        for (int j=0; j<m; j++)
            if (cells[i][j] == 0)
    {
        cells[i][j] = 2;
        vector<point> current_path = { {i, j} };

        while (true)
        {
            int move_id = rand() % moves.size();
            point p = {(current_path.back().x + moves[move_id].x + n)%n, (current_path.back().y + moves[move_id].y + m)%m};
            if (cells[p.x][p.y] == 2)
            {
                while (current_path.back() != p)
                {
                    cells[current_path.back().x][current_path.back().y] = 0;
                    current_path.pop_back();
                }
            }
            else
            {
                bool brk = (cells[p.x][p.y] == 1);
                cells[p.x][p.y] = 2;
                current_path.push_back(p);
                if (brk)
                    break;
            }
        }
        for (size_t i=0; i+1<current_path.size(); i++)
        {
            point p1 = current_path[i];
            point p2 = current_path[i+1];
            if ((p1.x + 1)%n == p2.x)
                maze.upper_walls[p2.x][p2.y] = 0;
            if ((p2.x + 1)%n == p1.x)
                maze.upper_walls[p1.x][p1.y] = 0;
            if ((p1.y + 1)%m == p2.y)
                maze.left_walls[p2.x][p2.y] = 0;
            if ((p2.y + 1)%m == p1.y)
                maze.left_walls[p1.x][p1.y] = 0;
        }
        for (auto p : current_path)
            cells[p.x][p.y] = 1;
    }
    return maze;
}

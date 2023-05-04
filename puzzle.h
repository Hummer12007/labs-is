#include <bits/stdc++.h>

class Puzzle
{
public:
    Puzzle(int n_, int m_, std::vector<std::vector<int> > rows, std::vector<std::vector<int> > columns);
    bool Solve();
    std::vector<std::vector<int> > GetGrid();
private:
    bool GoRow(int i);
    bool GoColumn(int i);
    int n, m;
    std::vector<std::vector<int> > a, b;
    std::vector<std::vector<int> > c;
};

#include <bits/stdc++.h>
#include <SFML/Graphics.hpp>
#include "labgen.h"
#include "astar.h"
#include "bfs.h"
#include <bits/stdc++.h>

using namespace std;

const int l = 10;
const int d = 1;
const int N = 100;
const int M = 100;
double lastmove = 0;
Maze m;
point mypos;
point targetpos;

void Update(const vector<point> path)
{
    if (path.size() == 1)
        return;

    if (clock()*1.0/CLOCKS_PER_SEC > lastmove + 0.05)
    {
        lastmove = clock()*1.0/CLOCKS_PER_SEC;
        mypos = path[1];
    }
}

void Draw(sf::RenderWindow* window, int x, int y, sf::Color c)
{
    sf::RectangleShape r;
    r.setPosition(y*l, x*l);
    r.setSize(sf::Vector2f(l, l));
    r.setFillColor(c);
    window->draw(r);
}

void Render(sf::RenderWindow* window)
{
    vector<point> path, visastar, visbfs;
    path = BFS(m, mypos, targetpos, visbfs);
    path = AStar(m, mypos, targetpos, visastar);
    Update(path);

    for (auto p : visbfs)
        Draw(window, p.x, p.y, sf::Color(255, 140, 0));
    for (auto p : visastar)
        Draw(window, p.x, p.y, sf::Color::Yellow);
    for (auto p : path)
        Draw(window, p.x, p.y, sf::Color::Green);
    for (auto p : {path[0], path.back()})
        Draw(window, p.x, p.y, sf::Color::Red);

    for (int i=0; i<=N; i++)
        for (int j=0; j<=M; j++)
    {
        if (m.left_walls[i%N][j%M])
        {
            sf::RectangleShape r;
            r.setPosition(j*l-d, i*l-d);
            r.setSize(sf::Vector2f(2*d, l+2*d));
            r.setFillColor(sf::Color::Black);
            window->draw(r);
        }
        if (m.upper_walls[i%N][j%M])
        {
            sf::RectangleShape r;
            r.setPosition(j*l-d, i*l-d);
            r.setSize(sf::Vector2f(l+2*d, 2*d));
            r.setFillColor(sf::Color::Black);
            window->draw(r);
        }
    }
}

#undef x
#undef y

int main()
{
    m = GenerateMaze(N, M);
    for (int _ = 0; _ < 1000; _ ++)
    {
        int i = rand()%N;
        int j = rand()%M;
        if (rand()%2)
            m.left_walls[i][j] = 0;
        else
            m.upper_walls[i][j] = 0;
    }
    mypos = targetpos = point{N/2, M/2};

    sf::RenderWindow window(sf::VideoMode(N*l, M*l), "Pacman", sf::Style::Close);
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
            if (event.type == sf::Event::MouseButtonPressed)
                if (event.mouseButton.button == sf::Mouse::Left)
            {
                targetpos.first = event.mouseButton.y / l;
                targetpos.second = event.mouseButton.x / l;
            }
        }

        window.clear(sf::Color::White);
        Render(&window);
        window.display();
    }

    return 0;
}

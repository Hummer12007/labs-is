#include "visual.h"

using namespace std;

void DrawPoint(point p, sf::RenderWindow* w, int wsize)
{
    sf::CircleShape c;
    c.setRadius(4);
    c.setPosition(p.x*wsize-4, p.y*wsize-4);
    w->draw(c);
}

void DrawLine(point p1, point p2, sf::RenderWindow* w, int wsize)
{
    sf::Vertex line[] =
    {
        sf::Vertex(sf::Vector2f(wsize*p1.x, wsize*p1.y)),
        sf::Vertex(sf::Vector2f(wsize*p2.x, wsize*p2.y))
    };
    w->draw(line, 2, sf::Lines);
}

void Display(int n, point* p, std::vector<int> order, sf::RenderWindow* window, int wsize)
{
    for (int i=0; i<n; i++)
        DrawPoint(p[i], window, wsize);
    for (int i=0; i<n; i++)
        DrawLine(p[order[i]], p[order[(i+1)%n]], window, wsize);
}

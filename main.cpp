#include "visual.h"

#define N_POINTS 200
#define N_POPULATION 100

using namespace std;
#define nmax 100500
int n;
point p[N_POINTS];

double pythagor(double dx, double dy)
{
    return sqrt(dx*dx + dy*dy);
}
double dist(int x, int y)
{
    return pythagor(p[x].x - p[y].x, p[x].y - p[y].y);
}
void gen(int n_)
{
    n = n_;
    for (int i=0; i<n; i++)
    {
        p[i].x = rand()*1.0/RAND_MAX;
        p[i].y = rand()*1.0/RAND_MAX;
    }
}
double dist(vector<int> v)
{
    double d = 0;
    for (int i=0; i<n; i++)
        d += dist(v[i], v[(i+1)%n]);
    return d;
}

int m;
vector<vector<int> > pop;
void init_population(int pop_size)
{
    m = pop_size;
    pop.resize(m);
    for (int i=0; i<m; i++)
    {
        for (int j=0; j<n; j++)
            pop[i].push_back(j);
        random_shuffle(pop[i].begin(), pop[i].end());
    }
}

double k = 1000;
int c = sqrt(N_POPULATION) - 1;
vector<double> dists;
vector<int> GetParent()
{
    double s = 0;
    for (int i=0; i<m; i++)
        s+=exp(-k*dists[i]);
    s = s*rand()/RAND_MAX;
    for (int i=0; i<m; i++)
    {
        s-=exp(-k*dists[i]);
        if (s <= 0)
            return pop[i];
    }
    return pop.back();
}

void Iteration()
{
    dists.assign(m, 0);
    for (int i=0; i<m; i++)
        dists[i] = dist(pop[i]);
    vector<vector<int> > new_pop;
    for (int i=0; i<m; i++)
    {
        vector<int> v;

        if (i < c)
            v = pop[i];
        else
        {
            v = GetParent();
            int r = rand()%2;
            if (r == 1)
            {
                int l = rand()%n;
                int r = rand()%n;
                if (l>r)
                    swap(l, r);
                reverse(v.begin()+l, v.begin()+r);
            }
            else
            {
                vector<int> u = GetParent();
                int l = rand()%n;
                int r = rand()%n;
                if (l>r)
                    swap(l, r);
                vector<int> used(n, 0);
                for (int i=0; i<l; i++)
                    used[v[i]] = 1;
                for (int i=r; i<n; i++)
                    used[v[i]] = 1;
                vector<int> uv;
                for (int i=0; i<l; i++)
                    uv.push_back(v[i]);
                for (int i=0; i<n; i++)
                    if (!used[u[i]])
                        uv.push_back(u[i]);
                for (int i=r; i<n; i++)
                    uv.push_back(v[i]);
                v = uv;
            }
        }

        new_pop.push_back(v);
    }
    sort(new_pop.begin(), new_pop.end(), [&](vector<int> v1, vector<int> v2){ return dist(v1) < dist(v2); });

    pop = new_pop;
}

int main()
{
    srand(time(0));
    gen(N_POINTS);
    init_population(N_POPULATION);

    int s = 1000;
    sf::RenderWindow window(sf::VideoMode(s, s), "SFML");
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear();
        Display(n, p, pop[0], &window, s);
        window.display();

        Iteration();
    }
    return 0;
}

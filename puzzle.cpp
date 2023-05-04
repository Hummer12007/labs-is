#include "puzzle.h"

using namespace std;

Puzzle::Puzzle(int n_, int m_, std::vector<std::vector<int> > rows, std::vector<std::vector<int> > columns)
{
    n = n_;
    m = m_;
    a = rows;
    b = columns;
    c.resize(n);
    for (int i=0; i<n; i++)
        c[i].assign(m, 0);
}

bool Puzzle::Solve()
{
    while (true)
    {
        try {
            bool ok = false;
            for (int i=0; i<n; i++)
                ok |= GoRow(i);
            for (int i=0; i<m; i++)
                ok |= GoColumn(i);
            if (!ok)
                break;
        }
        catch(int)
        {
            return false;
        }
    }

    for (int i=0; i<n; i++)
        for (int j=0; j<m; j++)
        {
            if (c[i][j] == 0)
            {
                Puzzle p = *this;
                p.c[i][j] = -1;
                if (p.Solve())
                {
                    c = p.c;
                    return true;
                }
                c[i][j] = 1;
                return Solve();
            }
        }
    return true;
}

std::vector<std::vector<int> > Puzzle::GetGrid()
{
    return c;
}

vector<int> LowestPossible(vector<int> v, vector<int> s)
{
    int n = v.size();
    int m = s.size();
    vector<int> u(n, -1);
    vector<int> p(m);
    int pos = 0;
    for (int i=0; i<m; i++)
    {
        int bad = 0;
        for (int j=pos; j<pos+s[i]; j++)
            bad += (v[j] == -1);
        while ((bad > 0) || (pos > 0 && v[pos-1] == 1) || (pos + s[i] < n && v[pos+s[i]] == 1))
        {
            if (pos + s[i] >= n)
                throw 0;
            bad -= (v[pos] == -1);
            bad += (v[pos+s[i]] == -1);
            pos++;
        }
        for (int j=pos; j<pos+s[i]; j++)
            u[j] = i;
        p[i] = pos;
        pos = pos+s[i]+1;
    }
    pos = m-1;
    int last = n+1;
    for (int i=n-1; i>=0; i--)
        if (i < last)
    if (v[i] == 1)
    {
        if (pos < 0)
            throw 0;
        if (p[pos]+s[pos]-1 >= i)
            break;

        for (int i=p[pos]; i<p[pos]+s[pos]; i++)
            u[i] = -1;
        p[pos] = i-s[pos]+1;
        last = p[pos];
        for (int i=p[pos]; i<p[pos]+s[pos]; i++)
            u[i] = pos;
    }
    return u;
}

vector<int> Go(vector<int> v, vector<int> s)
{ // process single line for guaranteed cells
//    for (int i : v)
//        cout<<" .#"[i+1];
//    cout<<"\n";
//    for (int i : s)
//        cout<<i<<" ";
//    cout<<"\n";

    int n = v.size();
    int m = s.size();

    vector<int> l = LowestPossible(v, s);
    reverse(v.begin(), v.end());
    reverse(s.begin(), s.end());
    vector<int> r = LowestPossible(v, s);
    reverse(v.begin(), v.end());
    reverse(s.begin(), s.end());
    reverse(r.begin(), r.end());
    for (int i=0; i<n; i++)
        if (r[i] >= 0)
            r[i] = m-1-r[i];

    int cl = -1;
    int cr = -1;
    for (int i=0; i<n; i++)
    {
        if (l[i]>=0 and r[i]>=0 and l[i]==r[i])
            v[i] = 1;
        if (l[i]>=0)
            cl = l[i];
        if (r[i]>=0)
            cr = r[i];
        if (l[i]==-1 and r[i]==-1 and cl == cr)
            v[i] = -1;
    }
    for (int i=0; i<n; i++)
        if (v[i] == 0)
            return v;
    int pos = 0;
    int cur = 0;
    for (int i=0; i<n; i++)
    {
        if (v[i] == 1)
            cur++;
        else if (cur > 0)
        {
            if (pos >= m || s[pos] != cur)
                throw 0;
            else
                pos++, cur=0;
        }
    }
    if ((cur > 0) && (pos >= m || s[pos] != cur))
        throw 0;
    return v;
}

bool Puzzle::GoRow(int i)
{
    vector<int> v(m);
    for (int j=0; j<m; j++)
        v[j] = c[i][j];
    v = Go(v, a[i]);
    bool f = false;
    for (int j=0; j<m; j++)
        if (v[j] != c[i][j])
        {
            if (c[i][j] != 0)
                throw 0;
            f = true, c[i][j] = v[j];
        }
    return f;
}
bool Puzzle::GoColumn(int i)
{
    vector<int> v(n);
    for (int j=0; j<n; j++)
        v[j] = c[j][i];
    v = Go(v, b[i]);
    bool f = false;
    for (int j=0; j<n; j++)
        if (v[j] != c[j][i])
        {
            if (c[j][i] != 0)
                throw 0;
            f = true, c[j][i] = v[j];
        }
    return f;
}

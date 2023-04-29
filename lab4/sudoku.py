#!/usr/bin/python3

from copy import deepcopy
from random import randint
from tkinter import *
            
def dbuddy(l, i, j):
    for k in range(9):
        if k != i and l[i][j][0] in l[k][j]:
            l[k][j].remove(l[i][j][0])
        if k != j and l[i][j][0] in l[i][k]:
            l[i][k].remove(l[i][j][0])
    for k in [3*(i//3), 3*(i//3)+1, 3*(i//3)+2]:
        for m in [3*(j//3), 3*(j//3)+1, 3*(j//3)+2]:
            if (k != i or m != j) and l[i][j][0] in l[k][m]:
                l[k][m].remove(l[i][j][0])

def contr(l):
    for i in range(9):
        for j in range(9):
            if len(l[i][j]) == 1:
                dbuddy(l, i, j)
            
def hsingle(l):
    l1 = []
    while l1 != l:
        l1 = deepcopy(l)
        for i in range(9):
            for n in list('123456789'):
                a, a1, a2 = 0, 0, 0
                for j in range(9):
                    if n in l[i][j]:
                        a1 += 1
                    if n in l[j][i]:
                        a2 += 1
                if a1 == 1:
                    for j in range(9):
                        if n in l[i][j]:
                            l[i][j] = [n]
                            dbuddy(l, i, j)
                            break
                if a2 == 1:
                    for j in range(9):
                        if n in l[j][i]:
                            l[j][i] = [n]
                            dbuddy(l, j, i)
                            break
                for k in [3*(i//3), 3*(i//3)+1, 3*(i//3)+2]:
                    for j in [(3*i)%9, (3*i)%9+1, (3*i)%9+2]:
                        if n in l[k][j]:
                            a += 1
                if a == 1:
                    for k in [3*(i//3), 3*(i//3)+1, 3*(i//3)+2]:
                        for j in [(3*i)%9, (3*i)%9+1, (3*i)%9+2]:
                            if n in l[k][j]:
                                l[k][j] = [n]
                                dbuddy(l, k, j)
                                break
        contr(l)

def npair(l):
    l1 = []
    while l1 != l:
        l1 = deepcopy(l)
        for i in range(9):
            p1, p2, p3, p11, p21, p31 = [], [], [], [], [], []
            for j in range(9):
                if len(l[i][j]) == 2:
                    p1.append(l[i][j])
                if len(l[j][i]) == 2:
                    p2.append(l[j][i])
            for j in p1:
                if p1.count(j)>1:
                    p11.append(j)
            for j in p2:
                if p1.count(j)>1:
                    p21.append(j)
            for k1 in p11:
                p1 = deepcopy(p11)
                p1.remove(k1)
                for k2 in p1:
                    if k1 == k2:
                        for j in range(9):
                            if k1[0] in l[i][j] and l[i][j] != k1:
                                l[i][j].remove(k1[0])
                            if k1[1] in l[i][j] and l[i][j] != k1:
                                l[i][j].remove(k1[1])
            for k1 in p21:
                p2 = deepcopy(p21)
                p2.remove(k1)
                for k2 in p2:
                    if k1 == k2:
                        for j in range(9):
                            if k1[0] in l[j][i] and l[j][i] != k1:
                                l[j][i].remove(k1[0])
                            if k1[1] in l[j][i] and l[j][i] != k1:
                                l[j][i].remove(k1[1])
            for k in [3*(i//3), 3*(i//3)+1, 3*(i//3)+2]:
                for j in [(3*i)%9, (3*i)%9+1, (3*i)%9+2]:
                    if len(l[k][j]) == 2:
                        p3.append(l[k][j])
            for j in p3:
                if p3.count(j)>1:
                    p31.append(j)
            for k1 in p31:
                p3 = deepcopy(p31)
                p3.remove(k1)
                for k2 in p3:
                    if k1 == k2:
                        for k in [3*(i//3), 3*(i//3)+1, 3*(i//3)+2]:
                            for j in [(3*i)%9, (3*i)%9+1, (3*i)%9+2]:
                                if k1[0] in l[k][j] and l[k][j] != k1:
                                    l[k][j].remove(k1[0])
                                if k1[1] in l[k][j] and l[k][j] != k1:
                                    l[k][j].remove(k1[1])
        contr(l)

def hpair(l):
    l1 = []
    while l1 != l:
        l1 = deepcopy(l)
        for i in range(9):
            p1, p2, p3 = [], [], []
            p11, p21, p31 = [], [], []
            p12, p22, p32  = [], [], []
            for n in list('123456789'):
                a = 0
                for j in range(9):
                    if n in l[i][j]:
                        a += 1
                if a == 2:
                    p1.append(n)
            for n in p1:
                for j in range(9):
                    if n in l[i][j]:
                        p11.append([i, j])
            for j in range(len(p11)):
                if j%2 == 0:
                    p12.append([p11[j], p11[j+1]])
            for j in range(len(p12)):
                p11 = deepcopy(p12)
                p11[j] = [0]
                for k in range(len(p11)):
                    if p11[k] == p12[j]:
                        l[p12[j][0][0]][p12[j][0][1]] = deepcopy([p1[j], p1[k]])
                        l[p12[j][1][0]][p12[j][1][1]] = deepcopy([p1[j], p1[k]])
            for n in list('123456789'):
                a = 0
                for j in range(9):
                    if n in l[j][i]:
                        a += 1
                if a == 2:
                    p2.append(n)
            for n in p2:
                for j in range(9):
                    if n in l[j][i]:
                        p21.append([j, i])
            for j in range(len(p21)):
                if j%2 == 0:
                    p22.append([p21[j], p21[j+1]])
            for j in range(len(p22)):
                p21 = deepcopy(p22)
                p21[j] = [0]
                for k in range(len(p21)):
                    if p21[k] == p22[j]:
                        l[p22[j][0][0]][p22[j][0][1]] = deepcopy([p2[j], p2[k]])
                        l[p22[j][1][0]][p22[j][1][1]] = deepcopy([p2[j], p2[k]])
            for n in list('123456789'):
                a = 0
                for k in [3*(i//3), 3*(i//3)+1, 3*(i//3)+2]:
                    for j in [(3*i)%9, (3*i)%9+1, (3*i)%9+2]:
                        if n in l[k][j]:
                            a += 1
                if a == 2:
                    p3.append(n)
            for n in p3:
                for k in [3*(i//3), 3*(i//3)+1, 3*(i//3)+2]:
                    for j in [(3*i)%9, (3*i)%9+1, (3*i)%9+2]:
                        if n in l[k][j]:
                            p31.append([k, j])
            for j in range(len(p31)):
                if j%2 == 0:
                    p32.append([p31[j], p31[j+1]])
            for j in range(len(p32)):
                p31 = deepcopy(p32)
                p31[j] = [0]
                for k in range(len(p31)):
                    if p31[k] == p32[j]:
                        l[p32[j][0][0]][p32[j][0][1]] = deepcopy([p3[j], p3[k]])
                        l[p32[j][1][0]][p32[j][1][1]] = deepcopy([p3[j], p3[k]])
        contr(l)
        for i in range(9):
            for j in range(9):
                l[i][j].sort()

def ppair(l):
    l1 = []
    while l1 != l:
        l1 = deepcopy(l)
        for i in range(9):
            for n in list('123456789'):
                a = 0
                p = []
                for k in [3*(i//3), 3*(i//3)+1, 3*(i//3)+2]:
                    for j in [(3*i)%9, (3*i)%9+1, (3*i)%9+2]:
                        if n in l[k][j]:
                            a += 1
                            p.append([k, j])
                if a == 2:
                    if p[0][0] == p[1][0]:
                        for j in range(9):
                            if (n in l[p[0][0]][j]
                                and 3*(p[0][0]//3)+(j//3) != i):
                                l[p[0][0]][j].remove(n)
                    if p[0][1] == p[1][1]:
                        for j in range(9):
                            if (n in l[j][p[0][1]]
                                and 3*(j//3)+(p[0][1]//3) != i):
                                l[j][p[0][1]].remove(n)
                if a == 3:
                    if p[0][0] == p[1][0] and p[0][0] == p[2][0]:
                        for j in range(9):
                            if (n in l[p[0][0]][j]
                                and 3*(p[0][0]//3)+(j//3) != i):
                                l[p[0][0]][j].remove(n)
                    if p[0][1] == p[1][1] and p[0][1] == p[2][1]:
                        for j in range(9):
                            if (n in l[j][p[0][1]]
                                and 3*(j//3)+(p[0][1]//3) != i):
                                l[j][p[0][1]].remove(n)
        for i in range(9):
            for n in list('123456789'):
                a = 0
                p = []
                for j in range(9):
                    if n in l[i][j]:
                        a += 1
                        p.append(j)
                if a == 2:
                    if p[0]//3 == p[1]//3:
                        t = 3*(i//3)+(p[0]//3)
                        for k in [3*(t//3), 3*(t//3)+1, 3*(t//3)+2]:
                            for j in [(3*t)%9, (3*t)%9+1, (3*t)%9+2]:
                                if n in l[k][j] and k != i:
                                    l[k][j].remove(n)
                if a == 3:
                    if p[0]//3 == p[1]//3 and p[0]//3 == p[2]//3:
                        t = 3*(i//3)+(p[0]//3)
                        for k in [3*(t//3), 3*(t//3)+1, 3*(t//3)+2]:
                            for j in [(3*t)%9, (3*t)%9+1, (3*t)%9+2]:
                                if n in l[k][j] and k != i:
                                    l[k][j].remove(n)
        for i in range(9):
            for n in list('123456789'):
                a = 0
                p = []
                for j in range(9):
                    if n in l[j][i]:
                        a += 1
                        p.append(j)
                if a == 2:
                    if p[0]//3 == p[1]//3:
                        t = 3*(p[0]//3)+(i//3)
                        for k in [3*(t//3), 3*(t//3)+1, 3*(t//3)+2]:
                            for j in [(3*t)%9, (3*t)%9+1, (3*t)%9+2]:
                                if n in l[k][j] and j != i:
                                    l[k][j].remove(n)
                if a == 3:
                    if p[0]//3 == p[1]//3 and p[0]//3 == p[2]//3:
                        t = 3*(p[0]//3)+(i//3)
                        for k in [3*(t//3), 3*(t//3)+1, 3*(t//3)+2]:
                            for j in [(3*t)%9, (3*t)%9+1, (3*t)%9+2]:
                                if n in l[k][j] and j != i:
                                    l[k][j].remove(n)
        contr(l)

def solve(l):
    contr(l)
    l2 = []
    while l2 != l:
        l2 = deepcopy(l)
        hsingle(l)
        npair(l)
        hpair(l)
        ppair(l)

def complete(l):
    b = True
    for i in range(9):
        for j in range(9):
            if len(l[i][j])>1:
                b = False
    return b

def ariadne(l):
    b = True
    while b:
        t = deepcopy(l)
        p = []
        for i in range(9):
            for j in range(9):
                if len(t[i][j])>1:
                    p .append([i, j])
        m = randint(0, len(p)-1)
        n = t[p[m][0]][p[m][1]][randint(0, len(t[p[m][0]][p[m][1]])-1)]
        t[p[m][0]][p[m][1]] = [n]
        solve(t)
        for i in range(9):
            for j in range(9):
                if len(t[i][j]) == 0:
                    b = False
        if b == False:
            l[p[m][0]][p[m][1]].remove(n)

def printl(l):
    s = [x[0] if len(x) == 1 else ' ' for i in range(9) for x in l[i]]
    q = lambda x,y: x+y+x+y+x
    r = lambda a,b,c,d,e: a+q(q(b*3,c),d)+e+"\n"
    print(r(*"┏━┯┳┓")+q(q("┃ %s │ %s │ %s "*3+"┃\n",r(*"┠─┼╂┨")),r(*"┣━┿╋┫"))%(*s,)+r(*"┗━┷┻┛"))

l, t = [], []
for i in range(9):
    l.append(list(input()))
for i in range(9):
    for j in range(9):
        if l[i][j] == '.':
            l[i][j] = list('123456789')
        else:
            t.append([i, j])
            l[i][j] = deepcopy([l[i][j]])

print("Input:")
printl(l)

while not complete(l):
    solve(l)
    if not complete(l):
        ariadne(l)

print("\nSolved:")
printl(l)

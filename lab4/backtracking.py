#!/usr/bin/python3
import numpy as np

def inc(i, j):
    if j < 8:
        j += 1
    elif i < 8:
        i += 1
        j = 0
    return i, j

def dec(i, j):
    if j > 0:
        j -= 1
    elif i > 0:
        i -= 1
        j = 8
    return i, j

def contr(s):
    
    def repeat(l):
        for i in range(9):
            for j in range(i+1, 9):
                if l[i] == l[j] and l[i] != 0:
                    return True
        return False

    for i in range(9):
        row = s[i, :]
        col = s[:, i]
        cell = s[3*(i//3):3*(i//3)+3, (3*i)%9:(3*i)%9+3].flatten()
        if repeat(row) or repeat(col) or repeat(cell):
            return True
    return False

def backtrack(s):
    i, j = 0, 0
    flag = False
    while 0 in s or contr(s):
        while (i, j) in fixed:
            i, j = inc(i, j)
        s[i][j] = 1
        while contr(s) or flag:
            if s[i][j] < 9:
                flag = False
                s[i][j] += 1
            else:
                flag = True
                s[i][j] = 0
                i, j = dec(i, j)
                while (i, j) in fixed:
                    i, j = dec(i, j)
        i, j = inc(i, j)

fixed = []
sudoku = []

for i in range(9):
    row = [i for i in input()]
    for j in range(9):
        if row[j] == '.':
            row[j] = '0'
        else:
            fixed.append((i, j))
    row = [int(i) for i in row]
    sudoku.append(row)

sudoku = np.array(sudoku)
backtrack(sudoku)

for row in sudoku:
    for i in row:
        print(i, end=' ')
    print()

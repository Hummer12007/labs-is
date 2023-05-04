# Pacman

Лаба 1 Редько Павло

## Шлях за DFS
Щоб запустити залежно від розміру лабіринту:

```python pacman.py -l tinyMaze -p SearchAgent```

```python pacman.py -l mediumMaze -p SearchAgent```

```python pacman.py -l bigMaze -z .5 -p SearchAgent```

## Pathfinding using BFS
Щоб запустити:

```python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs```

```python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5```

## Pathfinding A*
Щоб запустити: 

```python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic```

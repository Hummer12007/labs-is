from priorityqueue import PriorityQueue
from enum import Enum


class GhostChaseAlgorithm(Enum):
    ASTAR = "ASTAR"
    DIJKSTRA = "DIJKSTRA"


def reconstruct_path(came_from, start, end):
    """
    >>> came_from = {'b': 'a', 'c': 'a', 'd': 'c', 'e': 'd', 'f': 'd'}
    >>> reconstruct_path(came_from, 'a', 'e')
    ['a', 'c', 'd', 'e']
    """
    reverse_path = [end]
    while end != start:
        end = came_from[end]
        reverse_path.append(end)
    return list(reversed(reverse_path))


def equal_goal(cell, goal):
    return cell == (goal[0], goal[1])


def get_adjacent_cells(grid, cell):
    i, j = cell
    cells_list = []
    if 0 <= i + 1 < len(grid) and grid[i + 1][j] == 0:
        cells_list.append((i + 1, j))
    if 0 <= i - 1 < len(grid) and grid[i - 1][j] == 0:
        cells_list.append((i - 1, j))
    if 0 <= j + 1 < len(grid[0]) and grid[i][j + 1] == 0:
        cells_list.append((i, j + 1))
    if 0 <= j - 1 < len(grid[0]) and grid[i][j - 1] == 0:
        cells_list.append((i, j - 1))
    return cells_list


def get_manhattan_distance(cell, goal):
    (i, j) = cell
    return abs(goal[0] - i) + abs(goal[1] - j)


def a_star_graph_search(
        start,
        goal,
        grid
):
    visited = set()
    came_from = dict()
    distance = {start: 0}
    frontier = PriorityQueue()
    frontier.add(start)
    while len(frontier) > 0:
        node = frontier.pop()
        if node in visited:
            continue
        if equal_goal(node, goal):
            return reconstruct_path(came_from, start, node)
        visited.add(node)
        for successor in get_adjacent_cells(grid, node):
            frontier.add(
                successor,
                priority=distance[node] + 1 + get_manhattan_distance(successor, goal)
            )
            if (successor not in distance
                    or distance[node] + 1 < distance[successor]):
                distance[successor] = distance[node] + 1
                came_from[successor] = node
    return None


def dijkstra_graph_search(
        start,
        goal,
        grid
):
    visited = set()
    came_from = dict()
    distance = {start: 0}
    frontier = PriorityQueue()
    frontier.add(start)
    while len(frontier) > 0:
        node = frontier.pop()
        if node in visited:
            continue
        if equal_goal(node, goal):
            return reconstruct_path(came_from, start, node)
        visited.add(node)
        for successor in get_adjacent_cells(grid, node):
            frontier.add(
                successor,
                priority=distance[node] + 1
            )
            if (successor not in distance
                    or distance[node] + 1 < distance[successor]):
                distance[successor] = distance[node] + 1
                came_from[successor] = node
    return None


def shortestPathBinaryMatrix(grid, start, goal, chase_algorithm):
    if chase_algorithm == GhostChaseAlgorithm.ASTAR:
        shortest_path = a_star_graph_search(
            start,
            goal,
            grid
        )
    else:
        shortest_path = dijkstra_graph_search(
            start,
            goal,
            grid
        )

    if shortest_path is None:
        return []
    else:
        return shortest_path

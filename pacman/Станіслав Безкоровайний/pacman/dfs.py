import random

def nearby_ghosts(grid, x, y):
    for i in range(0,1):
        for j in range(0,1):
            r = i + x
            c = j + y
            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == 'G':
                return True 
    
    return False

# function to get valid neighbors of a cell in the grid
def get_neighbors(grid, row, col, ignoreGhosts, prevMove, depth):
    directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]

    random.shuffle(directions)

    # This intereting trick is needed to get pacman from being stuck
    if depth == 0:
        if prevMove == 'L':
            directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        elif prevMove == 'R':
            directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
        elif prevMove == 'D':
            directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        else:
            directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]

    neighbors = []
    for d in directions:
        r = row + d[0]
        c = col + d[1]
        if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] != 'W' and grid[r][c] != 'D':
            if ignoreGhosts or not nearby_ghosts(grid, r, c):
                neighbors.append((r, c))
    return neighbors

# function to perform DFS on the grid
def dfs(grid, curr_pos, end, visited, path, ignoreGhosts, prevMove):
    if curr_pos == end:
        return path
    visited.add(curr_pos)
    for neighbor in get_neighbors(grid, curr_pos[0], curr_pos[1], ignoreGhosts, prevMove, len(path)):
        if neighbor not in visited:
            move = get_move(curr_pos, neighbor)
            result = dfs(grid, neighbor, end, visited, path + move, ignoreGhosts, prevMove)
            if result:
                return result
    return None

# function to get the move needed to go from one cell to another
def get_move(curr_pos, next_pos):
    if curr_pos[0] == next_pos[0]:
        return 'R' if curr_pos[1] < next_pos[1] else 'L'
    else:
        return 'D' if curr_pos[0] < next_pos[0] else 'U'


from collections import deque

def nearby_ghosts(grid, x, y):
    for i in range(-1,2):
        for j in range(-1,2):
            r = i + x
            c = j + y
            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == 'G':
                return True 
    
    return False

# function to get valid neighbors of a cell in the grid
def get_neighbors(grid, row, col, ignoreGhosts):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
    neighbors = []
    for d in directions:
        r = row + d[0]
        c = col + d[1]
        if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] != 'W' and grid[r][c] != 'D':
            if grid[r][c] != 'G' or ignoreGhosts:
                neighbors.append((r, c))
    return neighbors

# function to perform BFS on the grid
def bfs(grid, start, end, ignoreGhosts):
    queue = deque([(start, "")])
    visited = set()
    while queue:
        curr_pos, curr_path = queue.popleft()
        if curr_pos == end:
            return curr_path
        if curr_pos in visited:
            continue
        visited.add(curr_pos)
        for neighbor in get_neighbors(grid, curr_pos[0], curr_pos[1], ignoreGhosts):
            queue.append((neighbor, curr_path + get_move(curr_pos, neighbor)))
    return None

def bfs_only_visit(grid, start, end, ignoreGhosts):
    queue = deque([(start, "")])
    visited = set()
    while queue:
        curr_pos, curr_path = queue.popleft()
        if curr_pos == end:
            return curr_path
        if curr_pos in visited:
            continue
        visited.add(curr_pos)
        for neighbor in get_neighbors(grid, curr_pos[0], curr_pos[1], ignoreGhosts):
            if not nearby_ghosts(grid, neighbor[0], neighbor[1]) or ignoreGhosts:
                queue.append((neighbor, curr_path + get_move(curr_pos, neighbor)))
    return visited

# function to get the move needed to go from one cell to another
def get_move(curr_pos, next_pos):
    if curr_pos[0] == next_pos[0]:
        return 'R' if curr_pos[1] < next_pos[1] else 'L'
    else:
        return 'D' if curr_pos[0] < next_pos[0] else 'U'

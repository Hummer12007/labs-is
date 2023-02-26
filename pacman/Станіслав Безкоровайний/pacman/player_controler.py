
import bfs
import dfs
import astar


asciiDraw = {
    "glasses": "L",
    "pellet": ".",
    "pellet-power": "*",
    "door-h": "d",
    "door-v": "D",
    "showlogo": "s",
    "hiscores": "h",
    "ghost-door": "H"
}

types = [
    "glasses", "pellet", "pellet-power", "door-h", "door-v", "showlogo", "hiscores", "ghost-door"
]

# This particular implementation uses BFS, but it wouldn't matter whether DFS or anything else
# is used. Its only purpose is to get the list of accessible nodes. The exact target is then selected
# based on the heuristic based on manhattan distance
def get_target(betterMap, ghosts, player, cur_target, game):
    _row = -1
    _col = -1

    max_points = -1000000000

    ignoreGhosts = False
    if game.ghostTimer > 80:
        ignoreGhosts = True

    # Just visit as much as possible
    visited_poss = bfs.bfs_only_visit(
        betterMap,
        (player.nearestRow, player.nearestCol),
        (0,0),
        ignoreGhosts
    )

    # Preserve current target when possible
    if cur_target is not None and cur_target in visited_poss:
        (cur_t_x, cur_t_y) = cur_target
        if betterMap[cur_t_x][cur_t_y] == '.' or betterMap[cur_t_x][cur_t_y] == '*':
            return cur_target

    for pos in visited_poss:
        cur = 0
        (i, j) = pos            
        t = betterMap[i][j]

        if t == '.' or t == '*':
            # The chances are inversely proportional to the distance from the pacman (basically
            # the pacman should try to chase the pellets that are close to it)
            cur += 100000 / ((abs(player.nearestRow - i)) + (abs(player.nearestCol - j)))

        for g in ghosts:
            ghost = ghosts[g]
            row = ghost.nearestRow
            col = ghost.nearestCol

            # The father from ghost the target is, the better
            cur -= abs(i - row) + abs(j - col)

        if cur > max_points:
            _row = i
            _col = j
            max_points = cur

    return [_row, _col]

def upd_list(field, col, row, val):
    r = list(field[row])
    r[col] = val

    field[row] = "".join(r)

# Transforms the current state of the game into a 2D grid whcih 
# is easy to use for DFS/BFS/A start algorithms
def mapTransform(level, tileID, ghosts, player):
    result = []
    for i in range(0, level.lvlHeight):
        outline = ''
        for j in range(0, level.lvlWidth):
            
            t = level.GetMapTile(i,j)
            found = False
            for type in types:
                if t == tileID[type]:
                    outline += asciiDraw[type]
                    found = True
                    break
            
            if t >= 100 and t <= 199 and not found:
                outline += 'W'
            elif not found:
                outline += ' '

        result.append(outline)

    for ghost in ghosts:
        col = ghosts[ghost].nearestCol
        row = ghosts[ghost].nearestRow
        upd_list(result, col, row, "G")
    
    upd_list(result, player.nearestCol, player.nearestRow, "P")

    return result            

class PlayerPathFindController:
    def __init__(self) -> None:
        super().__init__()
        self.target = None
    
    def next_move(self, level, player, ghosts, tileID, game):
        player.nearestRow = int(((player.y + 8) / 16))
        player.nearestCol = int(((player.x + 8) / 16))

        betterMap = mapTransform(level, tileID, ghosts, player)

        new_target = get_target(betterMap, ghosts, player, self.target, game)
        self.target = (new_target[0], new_target[1])

        next_move = self.next_move_based_on_target(
            betterMap,
            new_target,
            level,
            player,
            ghosts,
            game
        )

        return next_move

    def next_move_based_on_target(self, betterMap, target, level, player, ghosts):
        pass

class BFS(PlayerPathFindController):
    def next_move_based_on_target(self, betterMap, target, level, player, ghosts, game):
        ignoreGhosts = False
        if game.ghostTimer > 80:
            ignoreGhosts = True

        path = bfs.bfs(
            betterMap,
            (player.nearestRow, player.nearestCol),
            (target[0], target[1]),
            ignoreGhosts
        )

        normal_move = ''

        if len(path) != 0:
            normal_move = path[0]

        idealPlayerY = player.nearestRow * 16 
        idealPlayerX = player.nearestCol * 16

        # This is needed to ensure that the pacman fills the square it is in
        if idealPlayerX > player.x  and normal_move != 'L':
            return 'R'
        if idealPlayerX < player.x  and normal_move != 'R':
            return 'L'
        if idealPlayerY < player.y  and normal_move != 'D':
            return 'U'
        if idealPlayerY > player.y  and normal_move != 'U':
            return 'D'

        if len(normal_move) == 0:
            return 'L'
        
        return path[0]

class DFS(PlayerPathFindController):
    def __init__(self) -> None:
        super().__init__()

        self.prev_move = None
        self.second_prior = None

    def next_move_based_on_target(self, betterMap, target, level, player, ghosts, game):
        ignoreGhosts = False
        if game.ghostTimer > 80:
            ignoreGhosts = True

        path = dfs.dfs(
            betterMap,
            (player.nearestRow, player.nearestCol),
            (target[0], target[1]),
            set(),
            '',
            ignoreGhosts,
            self.prev_move
        )

        if path is None:
            path = ''

        normal_move = ''

        if len(path) != 0:
            normal_move = path[0]
            

        idealPlayerY = player.nearestRow * 16 
        idealPlayerX = player.nearestCol * 16


        # This is needed to ensure that the pacman fills the square it is in
        if idealPlayerX > player.x  and normal_move != 'L':
            self.prev_move = 'R'
            return 'R'
        if idealPlayerX < player.x  and normal_move != 'R':
            self.prev_move = 'L'
            return 'L'
        if idealPlayerY < player.y  and normal_move != 'D':
            self.prev_move = 'U'
            return 'U'
        if idealPlayerY > player.y  and normal_move != 'U':
            self.prev_move = 'D'
            return 'D'

        if len(normal_move) == 0:
            self.prev_move = 'L'
            return 'L'
        
        self.prev_move = path[0]
        return path[0]

class Astar(PlayerPathFindController):
    def next_move_based_on_target(self, betterMap, target, level, player, ghosts, game):
        ignoreGhosts = False
        if game.ghostTimer > 80:
            ignoreGhosts = True

        path = astar.astar(
            betterMap,
            (player.nearestRow, player.nearestCol),
            (target[0], target[1]),
            ignoreGhosts
        )

        normal_move = ''

        if len(path) != 0:
            normal_move = path[0]
            

        idealPlayerY = player.nearestRow * 16 
        idealPlayerX = player.nearestCol * 16

        # This is needed to ensure that the pacman fills the square it is in
        if idealPlayerX > player.x  and normal_move != 'L':
            return 'R'
        if idealPlayerX < player.x  and normal_move != 'R':
            return 'L'
        if idealPlayerY < player.y  and normal_move != 'D':
            return 'U'
        if idealPlayerY > player.y  and normal_move != 'U':
            return 'D'

        if len(normal_move) == 0:
            return 'L'
        
        return path[0]



# thisLevel.GetMapTile(randRow, randCol) == tileID[ 'pellet' ]




# glasses
# pellet
# pellet-power
# door-h
# door-v
# ghost-door 
# showlogo
# hiscores
# 

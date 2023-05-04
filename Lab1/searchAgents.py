from game import Directions
from game import Agent
from game import Actions
import util
import time
import search

class GoWestAgent(Agent):
    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        if Directions.WEST in state.getLegalPacmanActions():
            return Directions.WEST
        else:
            return Directions.STOP

class SearchAgent(Agent):

    def __init__(self, fn='depthFirstSearch', prob='PositionSearchProblem', heuristic='nullHeuristic'):
        # Warning: some advanced Python magic is employed below to find the right functions and problems
        self.fn = fn
        # Get the search function from the name and heuristic
        if fn not in dir(search):
            raise AttributeError(fn + ' is not a search function in search.py.')
        func = getattr(search, fn)
        if 'heuristic' not in func.__code__.co_varnames:
            print(('[SearchAgent] using function ' + fn))
            self.searchFunction = func
        else:
            if heuristic in list(globals().keys()):
                heur = globals()[heuristic]
            elif heuristic in dir(search):
                heur = getattr(search, heuristic)
            else:
                raise AttributeError(heuristic + ' is not a function in searchAgents.py or search.py.')
            print(('[SearchAgent] using function %s and heuristic %s' % (fn, heuristic)))
            # Note: this bit of Python trickery combines the search algorithm and the heuristic
            self.searchFunction = lambda x: func(x, heuristic=heur)

        # Get the search problem type from the name
        if prob not in list(globals().keys()) or not prob.endswith('Problem'):
            raise AttributeError(prob + ' is not a search problem type in SearchAgents.py.')
        self.searchType = globals()[prob]
        print(('[SearchAgent] using problem type ' + prob))

    def registerInitialState(self, state):
        if self.searchFunction == None: raise Exception("No search function provided for SearchAgent")
        starttime = time.time()
        problem = self.searchType(state) # Makes a new search problem
        self.actions  = self.searchFunction(problem) # Find a path
        totalCost = problem.getCostOfActions(self.actions)
        print(('Path found with total cost of %d in %.1f seconds' % (totalCost, time.time() - starttime)))
        if '_expanded' in dir(problem): print(('Search nodes expanded: %d' % problem._expanded))

    def getAction(self, state):
        if 'actionIndex' not in dir(self): self.actionIndex = 0
        i = self.actionIndex
        self.actionIndex += 1
        try:
            if i < len(self.actions):
                return self.actions[i]
            else:
                return Directions.STOP
        except TypeError:
            print("Exception: "+ self.fn + " did not return a list")
            exit()

class PositionSearchProblem(search.SearchProblem):

    def __init__(self, gameState, costFn = lambda x: 1, goal=(1,1), start=None, warn=True, visualize=True):
        self.walls = gameState.getWalls()
        self.startState = gameState.getPacmanPosition()
        if start != None: self.startState = start
        self.goal = goal
        self.costFn = costFn
        self.visualize = visualize
        if warn and (gameState.getNumFood() != 1 or not gameState.hasFood(*goal)):
            print('Warning: this does not look like a regular search maze')

        # For display purposes
        self._visited, self._visitedlist, self._expanded = {}, [], 0 # DO NOT CHANGE

    def getStartState(self):
        return self.startState

    def isGoalState(self, state):
        isGoal = state == self.goal

        # For display purposes only
        if isGoal and self.visualize:
            self._visitedlist.append(state)
            import __main__
            if '_display' in dir(__main__):
                if 'drawExpandedCells' in dir(__main__._display): #@UndefinedVariable
                    __main__._display.drawExpandedCells(self._visitedlist) #@UndefinedVariable

        return isGoal

    def getSuccessors(self, state):

        successors = []
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            x,y = state
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextState = (nextx, nexty)
                cost = self.costFn(nextState)
                successors.append( ( nextState, action, cost) )

        # Bookkeeping for display purposes
        self._expanded += 1 # DO NOT CHANGE
        if state not in self._visited:
            self._visited[state] = True
            self._visitedlist.append(state)

        return successors

    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions. If those actions
        include an illegal move, return 999999.
        """
        if actions == None: return 999999
        x,y= self.getStartState()
        cost = 0
        for action in actions:
            # Check figure out the next state and see whether its' legal
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
            cost += self.costFn((x,y))
        return cost

class StayEastSearchAgent(SearchAgent):
    def __init__(self):
        self.searchFunction = search.uniformCostSearch
        costFn = lambda pos: .5 ** pos[0]
        self.searchType = lambda state: PositionSearchProblem(state, costFn, (1, 1), None, False)

class StayWestSearchAgent(SearchAgent):
    """
    An agent for position search with a cost function that penalizes being in
    positions on the East side of the board.

    The cost function for stepping into a position (x,y) is 2^x.
    """
    def __init__(self):
        self.searchFunction = search.uniformCostSearch
        costFn = lambda pos: 2 ** pos[0]
        self.searchType = lambda state: PositionSearchProblem(state, costFn)

def manhattanHeuristic(position, problem, info={}):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

def euclideanHeuristic(position, problem, info={}):
    "The Euclidean distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return ( (xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2 ) ** 0.5

class CornersProblem(search.SearchProblem):
    """
    This search problem finds paths through all four corners of a layout.
    """

    def __init__(self, startingGameState):
        """
        Stores the walls, pacman's starting position and corners.
        """
        self.walls = startingGameState.getWalls()
        self.startingPosition = startingGameState.getPacmanPosition()
        top, right = self.walls.height-2, self.walls.width-2
        self.corners = ((1,1), (1,top), (right, 1), (right, top))
        for corner in self.corners:
            if not startingGameState.hasFood(*corner):
                print('Warning: no food in corner ' + str(corner))
        self._expanded = 0
        self.costFn = lambda x,y: 1


    def getStartState(self):
        """
        Returns the start state (in your state space, not the full Pacman state
        space)
        """
        
        corner_foods = []
        return (self.startingPosition, corner_foods)


    def isGoalState(self, state):
        position = state[0]
        corner_foods = state[1]
        return len(corner_foods) == 4


    def getSuccessors(self, state):

        """
        Returns successor states, the actions they require, and a cost of 1.
        """
        #print(self.corners[0] == (1,1))
        
        successors = []
        
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            "*** YOUR CODE HERE ***"
            x, y = state[0]
            suc_corners = []
            visited_corners = state[1]
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                next_state = (nextx, nexty)
                
                for each in visited_corners:
                    suc_corners.append(each)
                
                if next_state in self.corners:
                    if next_state not in suc_corners:
                        suc_corners.append(next_state)
                cost = self.costFn(nextx, nexty)
                successors.append( ((next_state, suc_corners), action, cost) )

            
        self._expanded += 1 # DO NOT CHANGE
        return successors

    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions.  If those actions
        include an illegal move, return 999999.  This is implemented for you.
        """
        if actions == None: return 999999
        x,y= self.startingPosition # from the starting point
        cost = 0

        for action in actions:
            dx, dy = Actions.directionToVector(action) # direction of the action
            x, y = int(x + dx), int(y + dy) # new position
            if self.walls[x][y]: return 999999 # hit wall
            cost += self.costFn(x,y) # add the cost on this new position
        return cost


def cornersHeuristic(state, problem):
    coordinates = state[0]
    visited_corners = state[1]
    unvisited_corners = []

    for one_corner in corners:
        if not one_corner in visited_corners:
            unvisited_corners.append(one_corner)

    heuristic_number = 0
        
    while len(unvisited_corners) != 0: # While not empty
        manhattan_distances = []
        # Get manhattan distance to every corner
        for each_corner in unvisited_corners:
            get_manhattan = util.manhattanDistance(coordinates, each_corner)
            manhattan_corner = (get_manhattan, each_corner)
            manhattan_distances.append(manhattan_corner)
        minimum, the_corner = min(manhattan_distances)
        coordinates = the_corner
        heuristic_number += minimum
        unvisited_corners.remove(the_corner)
            
    return heuristic_number
    


def mazeDistance(point1, point2, gameState):
    x1, y1 = point1
    x2, y2 = point2
    walls = gameState.getWalls()
    assert not walls[x1][y1], 'point1 is a wall: ' + str(point1)
    assert not walls[x2][y2], 'point2 is a wall: ' + str(point2)
    prob = PositionSearchProblem(gameState, start=point1, goal=point2, warn=False, visualize=False)
    return len(search.bfs(prob))

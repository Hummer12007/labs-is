import util

class SearchProblem:

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    fringe = util.Stack()
    visited_nodes = []
    get_start = problem.getStartState()
    directions = []
    # Initialize start state
    fringe.push( (get_start, []) )

    while not fringe.isEmpty():
        coordinates, directions = fringe.pop()
        # Return list of directions when goal met
        if problem.isGoalState(coordinates):
            return directions
        # Track visited states
        if not coordinates in visited_nodes:
            visited_nodes.append(coordinates)
        # Push successors to stack
        for successor, direction, placeholder in problem.getSuccessors(coordinates):
            if not successor in visited_nodes:
                fringe.push( (successor, directions + [direction]) )
            
    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    #Init required tools
    fringe = util.Queue()
    directions = []
    visited_states = []

    #Add start
    get_start = problem.getStartState()
    fringe.push( (get_start, []) )
    visited_states.append(get_start)

    while not fringe.isEmpty():
        
        get_state_xy, directions = fringe.pop()

        if problem.isGoalState(get_state_xy):
            return directions

        else:
            for successor, direction, cost in problem.getSuccessors(get_state_xy):
                # Track visited states
                if not successor in visited_states:
                    visited_states.append(successor)
                    fringe.push((successor, directions + [direction]))
                    #print(directions)
                
    return []
    util.raiseNotDefined()
    


def nullHeuristic(state, problem=None):
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):

    fringe = util.PriorityQueue()
    start_node = problem.getStartState()
    start_heuristic = heuristic(start_node, problem)
    visited_nodes = []
    fringe.push( (start_node, [], 0), start_heuristic)
    directions = []
    while not fringe.isEmpty():
        get_xy, directions, get_cost = fringe.pop()

        if problem.isGoalState(get_xy):
            return directions
        
        if not get_xy in visited_nodes:
            # Track visited_nodes
            visited_nodes.append(get_xy)
            
            for coordinates, direction, successor_cost in problem.getSuccessors(get_xy):
                if not coordinates in visited_nodes:
                    # Pass by reference
                    actions_list = list(directions)
                    actions_list += [direction]
                    # Get cost so far
                    cost_actions = problem.getCostOfActions(actions_list)
                    get_heuristic = heuristic(coordinates, problem)
                    fringe.push( (coordinates, actions_list, 1), cost_actions + get_heuristic)
    return []
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch

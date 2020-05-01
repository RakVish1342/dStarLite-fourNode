# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

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
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pathCostDict = {}
    prevSeen = []  # do not push nodes found in this list. "Discovered" nodes
    Fringe = util.PriorityQueue()
    startState = problem.getStartState()
    Fringe.push(startState, heuristic(startState, problem))
    pathCostDict[startState] = [[], 0]
    while not Fringe.isEmpty():
        # choose a child node from the fringe
        currentState = Fringe.pop()
        prevSeen.append(currentState)
        # if the child is a goal state return a solution
        if problem.isGoalState(currentState):
            print(">>>", pathCostDict[currentState][0])
            return pathCostDict[currentState][0]
        else:
            # expand the node
            # Note: getSuccessor might return even the wall states. Since registerInitialState() and observe()
            # functions are being used to only keep track of walls that have been encountered by the bot.
            children = problem.getSuccessors(currentState)
            # for each successor add to fringe iff it is not already expanded or in the fringe.

            for child in children:
                if child[0] not in prevSeen:
                    # for the child state append the action set to the current state
                    # with the action to the child.
                    h_val = heuristic(child[0], problem)
                    g_val = pathCostDict[currentState][1] + child[2]
                    f_val = h_val + g_val
                    if child[0] not in pathCostDict or g_val < pathCostDict[child[0]][1]:
                        # Currently storing the Manhattan path (ie. ignoring walls) to the given node due to local observability
                        # In pacman A*, where full awareness of the map was present, each step of this algo would store the true
                        #  path to that node (with wall considerations), and  nt the manhattan path.
                        pathCostDict[child[0]] = [pathCostDict[currentState][0]+[child[1]], g_val]

                    Fringe.update(child[0], f_val)
                    # For graph search to avoid loops add the child to the "discovered" node list
    return []


def dStarLite(problem, heuristic=nullHeuristic):
    print("TODO: DSTAR")








# Abbreviations
astar = aStarSearch
dlite = dStarLite

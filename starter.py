
# =================================================================================================
# ==== 3.1 ========================================================================================
# =================================================================================================

"""
This class stores information about the environment and the problem the agent is solving.
"""
class GridWorldEnv:

    # GridWorldState = (row, col) tuple

    ACTIONS = ['U', 'D', 'L', 'R']

    def __init__(self):
        # what information about the environment do you need to store for the agent to play?
        # indexing is top to bottom, left to right (row, column)
        
        self.obstacles = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 1, 1, 1, 1, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 1, 1, 1, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.costs = [[1, 1,  1,  5,  5,  5,  5, 1, 1],
                      [1, 1,  1,  5,  5,  5,  5, 1, 1],
                      [1, 1, 10, 10, 10, 10, 10, 1, 1],
                      [1, 1,  1, 10, 10, 10, 10, 1, 1],
                      [1, 1,  1,  1,  1, 10, 10, 1, 1],
                      [1, 1,  1,  1,  1, 10, 10, 1, 1],
                      [1, 1,  1,  1, 10, 10, 10, 1, 1],
                      [1, 1,  1, 10, 10, 10, 10, 1, 1],
                      [1, 1,  1,  1,  1,  1,  1, 1, 1]]

    def step(self, state, action):
        """
        :param state: (row, col) tuple
        :param action: 'U', 'D', 'L' or 'R'
        :return: (success [True/False], new state, action cost)
        """
        # how can you take a state and action and return the next state?
        # what happens in the case of an illegal action?
        pass # delete when implemented

    def is_goal(self, state):
        """
        :param state: (row, col) tuple
        :return: True/False
        """
        pass # delete when implemented

    def get_state_cost(self, state):
        pass # delete when implemented


"""
This class represents a state/node in a search tree or state graph
"""
class StateNode:

    def __init__(self):
        # what information does each state need so that your agent can search?
        pass # delete when implemented

    def get_successors(self):
        # how can you generate all children from a given node?
        pass # delete when implemented



def bfs():
    # uses a FIFO queue
    pass # delete when implemented


# for a good example of the algorithm, see https://www.youtube.com/watch?v=7QcoJjSVT38 @ 3:25
def iddfs():
    # uses a LIFO queue
    pass # delete when implemented


def depth_limited_dfs():
    pass # delete when implemented


# =================================================================================================
# ==== 3.2 ========================================================================================
# =================================================================================================

def ucs():
    pass # delete when implemented


def a_star():
    pass # delete when implemented


def heauristic():
    # what heuristic do you think would be best for this problem?
    # e.g. manhattan distance or euclidean distance?
    pass # delete when implemented

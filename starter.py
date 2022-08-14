
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


def grid_heauristic():
    # what heuristic do you think would be best for this problem?
    # e.g. manhattan distance or euclidean distance?
    pass # delete when implemented


# =================================================================================================
# ==== 3.2 ========================================================================================
# =================================================================================================


LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3


class EightPuzzle:

    def __init__(self, squares):
        self.squares = tuple(squares)

        idx = -1
        for i in range(len(self.squares)):
            if self.squares[i] == '_':
                idx = i
        self.idx = idx

    def __eq__(self, obj):
        if obj is None:
            return False
        return self.squares == obj.squares

    def __hash__(self):
        return hash(self.squares)

    def move_left(self):
        new_squares = list(self.squares)
        new_squares[self.idx] = self.squares[self.idx-1]
        new_squares[self.idx-1] = self.squares[self.idx]
        return EightPuzzle(new_squares)

    def move_right(self):
        new_squares = list(self.squares)
        new_squares[self.idx] = self.squares[self.idx+1]
        new_squares[self.idx+1] = self.squares[self.idx]
        return EightPuzzle(new_squares)

    def move_up(self):
        new_squares = list(self.squares)
        new_squares[self.idx] = self.squares[self.idx-3]
        new_squares[self.idx-3] = self.squares[self.idx]
        return EightPuzzle(new_squares)

    def move_down(self):
        new_squares = list(self.squares)
        new_squares[self.idx] = self.squares[self.idx+3]
        new_squares[self.idx+3] = self.squares[self.idx]
        return EightPuzzle(new_squares)

    def get_successors(self):
        successors = []

        if self.idx % 3 > 0:
            successors.append(self.move_left())
        else:
            successors.append(None)

        if self.idx % 3 < 2:
            successors.append(self.move_right())
        else:
            successors.append(None)

        if self.idx // 3 > 0:
            successors.append(self.move_up())
        else:
            successors.append(None)

        if self.idx // 3 < 2:
            successors.append(self.move_down())
        else:
            successors.append(None)

        return successors

    def num_inversions(self):
        total = 0
        for i in range(len(self.squares)):
            if self.squares[i] == '_':
                continue
            si = int(self.squares[i])
            for j in range(i, len(self.squares)):
                if self.squares[j] == '_':
                    continue
                sj = int(self.squares[j])
                if si > sj:
                    total += 1
        return total

    def get_parity(self):
        return self.num_inversions() % 2

    def __str__(self):
        s = ""
        for c in self.squares:
            s += c
        return s


class ContainerEntry:
    def __init__(self, puzzle, parent, action_from_parent):
        self.puzzle = puzzle
        self.parent = parent
        self.action_from_parent = action_from_parent

    def get_successors(self):
        s = []
        suc = self.puzzle.get_successors()

        if suc[0] is not None:
            s.append(ContainerEntry(suc[0], self, LEFT))
        if suc[1] is not None:
            s.append(ContainerEntry(suc[1], self, RIGHT))
        if suc[2] is not None:
            s.append(ContainerEntry(suc[2], self, UP))
        if suc[3] is not None:
            s.append(ContainerEntry(suc[3], self, DOWN))

        return s

    def __eq__(self, obj):
        return self.puzzle == obj.puzzle


def bfs(initial, goal):
    container = [ContainerEntry(initial, None, None)]
    visited = set([])

    i = 0
    while len(container) > 0:
        # expand node
        node = container.pop(0)
        if node.puzzle == goal:
            actions = []
            while node.action_from_parent is not None:
                actions.append(node.action_from_parent)
                node = node.parent
            return list(reversed(actions))

        # add successors
        suc = node.get_successors()
        for s in suc:
            if s.puzzle not in visited:
                container.append(s)
                visited.add(s.puzzle)
        i += 1

    return None


def puzzle_heauristic():
    # what heuristic do you think would be best for this problem?
    # e.g. hamming distance or manhattan distance?
    # how can you keep it admissible?
    pass # delete when implemented
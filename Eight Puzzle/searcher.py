#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Julia Bighetto
# email:
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###

    def __init__(self, depth_limit):
        """ constructs a new Searcher object by initializing the attributes
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit

    def add_state(self, new_state):
        """ takes a single State object called new_state and adds it to the
            Searcher's list of untested states
        """
        self.states += [new_state]

    def should_add(self, state):
        """ takes a State object called state and returns True if the called
            Searcher should add state to its list of untested states, and
            False otherwise
        """
        if self.depth_limit != -1: 
            if state.num_moves > self.depth_limit:
                return False
        elif state.creates_cycle() == True:
            return False
        return True

    def add_states(self, new_states):
        """ takes a list State objects called new_states and processes the
            elements of new_state
        """
        for l in range(len(new_states)):
            if self.should_add(new_states[l]) == True:
                self.add_state(new_states[l])
        
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s

    def find_solution(self, init_state):
        """ performs a full state-space search that begins at the specified
            initial state init_state and ends when the goal state is found or
            when the Searcher runs out of untested states
        """
        self.add_state(init_state)
        while len(self.states) != 0:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal() == True:
                return s
            else:
                self.add_states(s.generate_successors())
        return None                 # failure
    
    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    """ a class that perform breadth-first search, choosing one of the
        untested states that has the smallest depth
    """
    
    def next_state(self):
        """ overides the next_state method inherited from Searcher. This
            version follows FIFO ordering and remove the chosen state from
            the list of untested states before returning it
        """
        s = self.states[0]
        self.states.remove(s)   #is this right?
        return s

class DFSearcher(Searcher):
    """ a class that performs depth-first search instead of random search.
        It chooses one of the untested states that has the largest depth
    """

    def next_state(self):
        """ overides the next_state method inherited from Searcher. This
            version follows LIFO ordering and remove the chosen state from
            the list of untested states before returning it
        """
        s = self.states[-1]
        self.states.remove(s)   #is this right?
        return s

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###

def h1(state):
    """ takes a State object called State and computes and returns
        an estimate of how many additional moves are needed to get
        from state to the original goal state
        estimate is the number of misplaced tiles in the Board object
        associated with state
    """
    misplaced = state.board.num_misplaced()
    return misplaced

def h2(state):
    """ takes a state object and returns a new estimate of now many
        additional moves are needed to get from state to the original
        goal state
    """
    misplaced2 = state.board.num_misplaced_2()
    return misplaced2
    
class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###

    def __init__(self, heuristic):
        """ constructs a new GreedySearcher object
        """
        super().__init__(-1)
        self.heuristic = heuristic

    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)

    def add_state(self, state):
        """ overrides the add_state method inherited from Searcher. This
            method adds a sublist that is a [priority, state] pair, where
            priority is the priority of state
        """
        self.states += [[self.priority(state), state]]

    def next_state(self):
        """ overrides the next_state method inherited from Searcher. This
            version of next_state chooses one of the state with the highest
            priority
        """
        thisone = max(self.states)
        self.states.remove(thisone)
        return thisone[1]
    
    def __repr__(self):
        """ returns a string representation of the greedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###

class AStarSearcher(Searcher):
    """ searcher object that performs A* search
    """
    
    def __init__(self, heuristic):
        """ constructs a new A*Search object
        """
        super().__init__(-1)
        self.heuristic = heuristic

    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher and the
        cost that has already been expended to get to that state
        """
        return -1 * (self.heuristic(state) + state.num_moves)

    def add_state(self, state):
        """ overrides the add_state method inherited from Searcher. This
            method adds a sublist that is a [priority, state] pair, where
            priority is the priority of state
        """
        self.states += [[self.priority(state), state]]

    def next_state(self):
        """ overrides the next_state method inherited from Searcher. This
            version of next_state chooses one of the state with the highest
            priority
        """
        thisone = max(self.states)
        self.states.remove(thisone)
        return thisone[1]


    
    def __repr__(self):
        """ returns a string representation of the greedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s

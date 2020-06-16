#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Julia Bighetto
# email:
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        height = len(self.tiles)
        width = len(self.tiles[0])
        for r in range(height):
            for c in range(width):
                number = int(digitstr[(3*r + c)])
                self.tiles[r][c] = number
                if number == 0:
                    self.blank_r = r
                    self.blank_c = c

    ### Add your other method definitions below. ###

    def __repr__(self):
        """ returns a string representation of a Board object
        """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == 0:
                    s += '_ '
                else:
                    s += str(self.tiles[r][c]) + ' '
            s += '\n'
        return s 

    def move_blank(self, direction): 
        """ takes as input a string direction that specifies the direction in which
            the blank should move, and the attempts to modify the contents of the called
            Board object accordingly
        """
        blankspace = self.tiles[self.blank_r][self.blank_c]
        if direction == 'left':
            if self.blank_c - 1 < 0:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c-1]
                self.tiles[self.blank_r][self.blank_c-1] = blankspace
                self.blank_c -= 1
                return True
        elif direction == 'right':
            if self.blank_c + 1 > 2:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c+1]
                self.tiles[self.blank_r][self.blank_c+1] = blankspace
                self.blank_c += 1
                return True
        elif direction == 'down':
            if self.blank_r + 1 > 2:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r+1][self.blank_c]
                self.tiles[self.blank_r+1][self.blank_c] = blankspace
                self.blank_r += 1
                return True
        elif direction == 'up':
            if self.blank_r -1 < 0:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r-1][self.blank_c]
                self.tiles[self.blank_r-1][self.blank_c] = blankspace
                self.blank_r -= 1
                return True
        else:
            print('unknown direction:', direction)
            return False

    def digit_string(self):
        """ creates and returns a string of digits that corresponds to the current
            contents of the called board object's tiles attribute
        """
        string = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                string += str(self.tiles[r][c])
        return string

    def copy(self): 
        """ returns a newly-constructed Board object that is a deep copy of the called
            object
        """
        newboard = Board(self.digit_string())
        return newboard

    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board object that
            are not where they should be in the goal state
        """
        currentboard = self.digit_string()
        goalboard = '012345678'
        misplacednums = 0
        for i in range(len(currentboard)):
            if currentboard[i] != goalboard[i]:
                if currentboard[i] == '0':
                    misplacednums += 0
                else:
                    misplacednums += 1
                
        return misplacednums
        
    def __eq__(self, other): 
        """ overloads the == operator and returns True if the called object self and the
            argument other have the same values for the tiles attribute, and False
            otherwise
        """
        if self.tiles == other.tiles:
            return True
        else:
            return False

    # helper function for h2

# a 2-D list that corresponds to the goal board (same as state, used for h2)

# function for h2
    def num_misplaced_2(self):
        """ returns a new number as priority. If a number is not at the correct
            place (using GOAL_TITLES as reference), num_misplaced_2 will get the
            necessary value from the correct column and row. 
        """
        goal_tiles = [[0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8]]
        
        newpriority = 0
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                board_tiles = self.tiles[row][col]
                if board_tiles != goal_tiles[row][col]:
                    newpriority += abs(row - board_tiles // 3)
                    newpriority += abs(col - board_tiles % 3)
                else:
                    None
        return newpriority
    
 #   def num_misplaced_2(self):
        """ returns a new number as priority. If a number is not at the correct
            place (using GOAL_TITLES as reference), num_misplaced_2 will get the
            necessary value from the correct column and row. 
        """
#        newpriority = 0
#        for row in range(len(self.tiles)):
#            for col in range(len(self.tiles[0])):
#                board_tiles = self.tiles[r][c]
#                if board_tiles != goal_tiles[r][c]:
#                    goalrow = abs(r - num // 3)
#                    goalcol = abs(c - num % 3)
#                    newpriority += goalrow
#                    newpriority += goalcol
#                else:
#                    None
#        return newpriority
                          

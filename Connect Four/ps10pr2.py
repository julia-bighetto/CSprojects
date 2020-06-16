#
# ps10pr2.py  (Problem Set 10, Problem 2)
#
# A Connect-Four Player class   
#

from ps10pr1 import Board

# write your class below

class Player:
    def __init__(self, checker):
        """ constructs a new Player obejct
        """
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ returns a string representing a Player object
        """
        s = 'Player ' + self.checker
        return s

    def opponent_checker(self):
        """ returns a one-character string representing the checker of
            the Player object's opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        """ accepts a Board object as a parameter and returns the
            colum where the player wants to make the next move
        """
        choice = int(input('Enter a column: '))
        if board.can_add_to(choice) == True:
            self.num_moves += 1
            return (choice)
        else:
            while board.can_add_to(choice) == False:
                print('Try again!')
                choice = int(input('Enter a column: '))
            self.num_moves += 1
            return (choice)
            
        

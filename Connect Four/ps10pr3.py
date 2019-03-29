#
# ps10pr3.py  (Problem Set 10, Problem 3)
#
# Playing the game    
#

from ps10pr1 import Board
from ps10pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1 not in 'XO' or player2 not in 'XO' \
       or player1 == player2:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

def process_move(player, board):
    """ takes two parameters and performs all of the steps involved in
        processing a single move by the specified player on the specified
        board
    """
    print (player, "'s turn") # why a space
    next_player_move = player.next_move(board)
    board.add_checker(player.checker, next_player_move)
    print()
    print(board)
    print()
    if board.is_win_for(player.checker) == True:
        print (player, 'wins in', player.num_moves, 'moves.')
        print ('Congratulations!')
        return True
    else:
        if board.is_full() == False:
            return False
        else:
            print ("It's a tie!")
            return True


class RandomPlayer(Player):

    def next_move(self, board):
        """ overrides the next_move method inherited from Player and chooses
            at random from the columns in the specified board that are not
            full yet and returns the index of that randomly selected column
        """
        num_moves_rp = 0
        listindex = []
        for i in range(board.width):
            if board.can_add_to(i) == True:
                listindex += [i]
        randomchoice = random.choice(listindex)
        self.num_moves += 1
        return randomchoice

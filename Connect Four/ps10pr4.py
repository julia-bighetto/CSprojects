#
# ps10pr4.py  (Problem Set 10, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps10pr3 import *

class AIPlayer(Player):

    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ returns a string representing an AIPlayer object
        """
        s = ''
        s += 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return s

    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of
            the board, and that returns the index of the column with the
            maximum score. If one or more columns are tied for the maximum
            score, the method should apply the called AIPlayer's tiebreaking
            strategy to break the tie
        """
        best_columns = max(scores) 
        indiceslist = []
        for i in range(len(scores)):
            if scores[i] == best_columns:
                indiceslist += [i]
        if len(indiceslist) == 1:
            return indiceslist[0]
        else:
            if self.tiebreak == 'LEFT':
                return indiceslist[0]
            elif self.tiebreak == 'RIGHT':
                return indiceslist[-1]
            elif self.tiebreak == 'RANDOM':
                return random.choice(indiceslist)

    def scores_for(self, board):
        """ takes a Board object board and determines the called AIPlayer's
            scores for the columns in board
        """
        scores = [50] * board.width
        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1 
            elif board.is_win_for(self.checker) == True:
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()) == True: 
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opp_scores = opponent.scores_for(board)
                index = self.max_score_column(opp_scores)
                if opp_scores[index] == 50:
                    scores[col] = 50
                elif opp_scores[index] == 100:
                    scores[col] = 0
                elif opp_scores[index] == 0:
                    scores[col] = 100
                board.remove_checker(col)
        self.num_moves += 1
        return scores

    def next_move(self, board):
        """ overrides the next_move method inherited from Player. This version
            returns the called AIPlayer's judgment of its best possible move
        """
        scores_list = self.scores_for(board)
        best_score = self.max_score_column(scores_list)
        return best_score
        # number of moves that should be returned?

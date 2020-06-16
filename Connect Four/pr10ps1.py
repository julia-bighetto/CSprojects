class Board:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.slots = [[' '] * width for row in range(self.height)]

    def __repr__(self): 
        s = ''
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
        s += ('-' * self.width * 2 + '-')
        s += '\n'
        for col in range(self.width):
            s += ' ' + str(col % 10)      
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker to column col of the called Board
            object
            inputs: column: a valid column from the board
                    checker: 'X' or 'O'
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        row = 0
        while row < self.height and self.slots[row][col] == ' ':
            row += 1
        self.slots[row - 1][col] = checker

    def reset(self):
        """ reset the Board object on which it is called by setting all
            slots to contain a space character
        """
        for c in range(self.width):
            for r in range(self.height):
                self.slots[r][c] = ' '

    def add_checkers(self, columns):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
        """
        checker = 'X'
        for col_str in columns:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
            if checker == 'X':
                checker = 'O'
            else:
                checker ='X'

    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the
            column col on the calling Board object. It will return
            False otherwise
        """
        if self.width - 1 < col:
            return False
        elif col < 0:
            return False
        else:
            if self.slots[0][col] == ' ':
                return True
            else:
                return False

    def is_full(self):
        """ returns True if the called Board object is completely full
            of checkers and returns False otherwise
        """
        for c in range(self.width):
            for r in range(self.height):
                if self.slots[r][c] == ' ':
                    return False
        return True

    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board
            object
        """
        assert(0 <= col < self.width)
        row = 0
        while row < self.height and self.slots[row][col] == ' ':
            row += 1
        if row < self.height:
            self.slots[row][col] = ' '
 
    def is_win_for(self, checker):
        """ accepts a parameter checker and returns True if there are
            four consecutive slots containing checker on the board. It
            returns False otherwise
            input: checkers: either X or O
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a down diagonal win for the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col - 1] == checker and \
                   self.slots[row - 2][col - 2] == checker and \
                   self.slots[row - 3][col - 3] == checker:
                    return True
        return False

    def is_up_diagonal_win(self, checker):
        """ Checks for an up diagonal win for the specified checker
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False

#
# ps8pr3.py  (Problem Set 8, Problem 3)
#
# Matrix Operations  
#
# Computer Science 111   
# 

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Enter a new matrix')
    print('(1) Negate the matrix')
    print('(2) Multiply a row by a constant')
    print('(3) Add one row to another')
    print('(4) Add a multiple of one row to another')
    print('(5) Transpose the matrix')
    print('(6) Quit')
    print()

def print_matrix(matrix):
    """ prints the specified matrix in rectangular form.
        input: matrix is a rectangular 2-D list numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print('%6.2f' % matrix[r][c], end=' ')
        print()
       
def get_matrix():
    """ gets a new matrix from the user and returns it
    """
    matrix = eval(input('Enter a new 2-D list of numbers: '))
    return matrix

def negate_matrix(matrix):
    """ negates all of the elements in the specified matrix
        inputs: matrix is a rectangular 2-D list of numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] *= -1
    # We don't need to return the matrix!
    # All changes to the matrix will still be there when the
    # function returns, because we received a copy of the
    # *reference* to the matrix used by main().

### Add your functions for options 2-5 here. ###

def mult_row(matrix, r, m):
    """ multiplies row r of the specified matrix by the specified multiplier m
        inputs: m is any type of number
    """
    height = len(matrix) + 1
    width = len(matrix[0])
    for c in range(width):
        matrix[r][c] *= m

def add_row_into(matrix, source, dest):
    """ takes the specified 2-D list matrixs and adds each element of the row
        with index source (the source row) to the corresponding source of the row
        with index dest (the destination row)
    """
    height = len(matrix)
    width = len(matrix[0])
    for c in range(width):
        matrix[dest][c] += matrix[source][c]
        
def add_mult_row_into(matrix, m, source, dest):
    """ takes the speficied 2-D list and adds each element of row source, multiplied
        by m, to the corresponding element of row dest
    """
    height = len(matrix)
    width = len(matrix[0])
    for c in range(width):
        matrix[dest][c] += matrix[source][c] * m

def transpose(matrix):
    """ takes the specified 2-D list matrix and creates and returns a new 2-D list
        that is the transpose of matrix
    """
    height = len(matrix)
    width = len(matrix[0])
    newheight = width
    newwidth = height
    newmatrix = []
    for r in range(newheight):
        row = [0] * newwidth
        newmatrix += [row]
    for r in range(height):
        for c in range(width):
            newmatrix[c][r] = matrix[r][c]
    return newmatrix
    
def main():
    """ the main user-interaction loop
    """
    ## The default starting matrix.
    ## DO NOT CHANGE THESE LINES.
    matrix = [[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]]

    while True:
        print()
        print_matrix(matrix)
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            matrix = get_matrix()
        elif choice == 1:
            negate_matrix(matrix)

        ## add code to handle the other options here
        elif choice == 2:
            choice1 = int(input('Index of row: '))
            r = choice1
            choice2 = float(input('Multiplier: '))
            m = choice2
            mult_row(matrix, r, m)
        elif choice == 3:
            choice3 = int(input('Index of source row: '))
            source = choice3
            choice4 = int(input('Index of destination row: '))
            dest = choice4
            add_row_into(matrix, source, dest)
        elif choice == 4:
            choice6 = int(input('Index of source row: '))
            source = choice6
            choice7 = int(input('Index of destination row: '))
            dest = choice7
            choice5 = float(input('Multiplier: '))
            m = choice5
            add_mult_row_into(matrix, m, source, dest)
        elif choice == 5:
            matrix = transpose(matrix)
        elif choice == 6:
            break
        else:
            print('Invalid choice. Try again.')

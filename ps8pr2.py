#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# Conway's Game of Life
#
# Computer Science 111  
#

# IMPORTANT: this file is for your solutions to Problem 2.
# Your solutions to Problem 1 should go in ps8pr1.py instead.

from ps8pr1 import *
from gol_graphics import *

def inner_reverse(grid):
    """ takes an existing generation of cells and creates and returns a new
        generation with the same dimensions as grid but in which the inner
        cells are the reverse of the inner cells in grid
        inputs: cells are either 0 or 1
    """
    new_grid = copy(grid)
    height = len(new_grid)
    width = len(new_grid[0])
    for r in range(1, height - 1):
        for c in range(1, width - 1):
            if grid[r][c] == 1:
                grid [r][c] = 0
            else:
                grid[r][c] = 1
    return grid

def count_neighbors(cellr, cellc, grid):
    """returns the number of alive neighbors of the cell at position [cellr]
        [cellc] in the specified grid
        inputs: cellr and cellc: always are one of the innter cells of grid
    """
    count = 0
    if grid[cellr-1][cellc-1] == 1:
#        print ('add one 1')
        count += 1
    if grid[cellr-1][cellc] == 1:
#        print ('add one2')
        count += 1
    if grid[cellr-1][cellc+1] == 1:
#        print ('add one3')
        count += 1
    if grid[cellr][cellc-1] == 1:
#        print ('add one4')
        count += 1
    if grid[cellr][cellc+1] == 1:
#        print ('add one5')
        count += 1
    if grid[cellr+1][cellc-1] == 1:
#        print ('add one6')
        count += 1
    if grid[cellr+1][cellc] == 1:
#        print ('add one7')
        count += 1
    if grid[cellr+1][cellc+1] == 1:
#        print ('add one8')
        count += 1
    return count

def next_gen(grid): #help
    """ takes a 2-d list grid that represents the current generations of cells
        and uses the rules of the Game of Life to create and return a new 2-d
        list representing the next generation of cells
    """
    newgrid = copy(grid)
    height = len(newgrid)
    width = len(newgrid[0])
    for c in range(1, height - 1):
        for r in range(1, width - 1):
            numberofneighbors = count_neighbors(r, c, grid)
            if numberofneighbors > 3:
                newgrid[r][c] = 0
            if numberofneighbors < 2:
                newgrid[r][c] = 0
            if grid[r][c] == 0 and numberofneighbors == 3:
                newgrid[r][c] = 1
    return newgrid
    
    

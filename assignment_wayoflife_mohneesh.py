"""

Conway's Way of Life
--------------------

Rule 1: Any live cell with fewer than two live neighbors dies, because of under
        population.
Rule 2: Any live cell with two or three live neighbors, lives on to the next generation.
Rule 3: Any live cell with more than three live neighbors dies, because of overpopulation.
Rule 4: Any dead cell with exactly three live neighbors becomes a live cell, because of
        reproduction.

Date: 29-03-2018
Programmer: S.Mohneesh
For further details see the README

"""
import argparse
import numpy as np

# take input as old_generation command line argument.
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="give the file name")
args = vars(ap.parse_args())
f = open(args['file'])                      # open the file
matrix = f.read()                           # read the matrix
f.close()

# converting the text into numpy array.
c=0
matrix = list(matrix)
for i in matrix[0:-1]:
    if i == '\n':
        c+=1                                # find shape
matrix = [x for x in matrix if x!='\n']     # removing '\n' 
matrix = np.array(matrix,dtype=int)
matrix.shape = (c+1,c+1)                    # reshaping



def game_of_life(a):
    xmax, ymax = a.shape
    b = a.copy()                            # Copying the grid and the rule 2 is implicit
    for x in range(xmax):
        for y in range(ymax):
            n = np.sum(a[max(x - 1, 0):min(x + 2, xmax), max(y - 1, 0):min(y + 2, ymax)]) - a[x, y]     # this is where we calculate the sum around the cell.
            if a[x, y]:
                if n < 2 or n > 3:
                    b[x, y] = 0             # the Rule 1 and 3
            elif n == 3:
                b[x, y] = 1                 # the Rule 4
    return(b)

for i in range(1):                          # Set how many generations you wish to see
    matrix = game_of_life(matrix)
    print('\n'.join(''.join('%d' %x for x in y) for y in matrix))                                       # printing in the desired way.
    print("\n")

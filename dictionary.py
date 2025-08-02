# letter = {"a":["undefined","undefined","ff2500","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined",
#           "undefined","ff2500","undefined","undefined","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined",
#           "undefined","ff2500","undefined","undefined","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined",
#           "undefined","ff2500","ff2500","ff2500","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined",
#           "undefined","ff2500","undefined","undefined","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined",
#           "undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined",
#           "undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined",
#           "undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined",
#           "undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined",
#           "undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined",
#           "undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined",
#           "undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined",
#           "undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined",
#           "undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined",
#           "undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined",
#           "undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined"]}


def overlay(grid, letter, line):
    """ the grid is my 32w x 16h LED display -1 denotes undefined, 1 is lit with a color, 0 is black, this display can write 2 lines, line can be 0,1"""

    row = 0
    col = 0

    while row < len(grid):
        while col < len(grid[row]):
            if line == 0 and 1 <= row <= 7 and grid[row][col] == -1:
                z = 0
                while z < len(letter[row-1]):
                    grid[row][col] = letter[row-1][z]
                    z += 1
                    col += 1
                row += 1
                col = 0
            elif line == 1 and 9 <= row <= 15 and grid[row][col] == -1:
                z = 0
                while z < len(letter[row-9]):
                    # print(row)
                    grid[row][col] = letter[row-9][z]
                    z += 1
                    col += 1
                if row <15:
                    row += 1
                else:
                    break
                col = 0
            else:
                col += 1
            # print(f"{row},{col}")
        col = 0
        row += 1

    for w in grid:
        print(w)

    return grid


grid = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

a = [[0,1,1,0,0],
     [1,0,0,1,0],
     [1,0,0,1,0],
     [1,1,1,1,0],
     [1,0,0,1,0],
     [1,0,0,1,0],
     [1,0,0,1,0]]

space = [[0],
         [0],
         [0],
         [0],
         [0],
         [0],
         [0]]

# testing section
grid = overlay(grid, a, 1) # push a letter

grid = overlay(grid, space, 1) # push a space

grid = overlay(grid, a, 1) # push a letter


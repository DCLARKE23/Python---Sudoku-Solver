#initialize hardcoded grid
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

#function to display board neatly
def display_board(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - + - - - + - - - ") #horizontal dividing lines

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="") #vertical dividing lines

            if j == 8:
                print(grid[i][j])
            else:
                print(f'{grid[i][j]} ', end="")

#handle initial print
print("This is the initial grid where 0 represents an empty space")
print()
display_board(grid)

def solve_sudoku(grid):
    has_empty_space = find_empty(grid)  #returns False if no empty spaces found, else (row, col)
    
    #if an empty space exists in grid, then assign coordinates to has_empty_space, otherwise return True, grid is solved
    if not has_empty_space:
        return True
    else:
        row, col = has_empty_space
   
    # Test values 1 - 9
    # Check if a given space is valid with a given num
    # if it is valid, set that space = num
    # check if the sudoku is solved, and if so return True
    # if not, clear the space and try with a different number
    # if num = 9 and it fails, it cannot be solved in that instance
    for num in range(1,10):
        if safe(grid, row, col, num):
            grid[row][col] = num
            
            if solve_sudoku(grid):
                return True

            grid[row][col] = 0
    return False 


def safe(grid,row,col,num):

    #check row
    for i in range(9):
        if grid[row][i] == num:
            return False
    #check column
    for i in range(9):
        if grid[i][col] == num:
            return False
    #check box
    #calculate which box to check
    box_row = row//3 * 3
    box_col = col//3 * 3

    for i in range(3):
        for j in range(3):
            if grid[i+box_row][j+box_col] == num:
                return False
    return True

#function to determine whether or not the board has any empty spaces
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return False

#handle final print or error
has_solution = solve_sudoku(grid)
if not has_solution:
    print("/n No Solution")
else:
    print()
    print("This is the solved board")
    print()
    display_board(grid)
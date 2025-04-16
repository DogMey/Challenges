import random

N = 3
EMPTY = 0

def printSudoku(sudoku):
    for i in range(N):
        for j in range(N):
            print(sudoku[i][j], end=" ")
        print()

def isValid(sudoku, row, col, num):
    # check row
    for j in range(N):
        if sudoku[row][j] == num:
            return False

    # check column
    for i in range(N):
        if sudoku[i][col] == num:
            return False

    # check sub-grid
    subgrid_row = row // 3
    subgrid_col = col // 3
    for i in range(subgrid_row * 3, subgrid_row * 3 + 3):
        for j in range(subgrid_col * 3, subgrid_col * 3 + 3):
            if sudoku[i][j] == num:
                return False

    return True

def solveSudoku(sudoku):
    row = -1
    col = -1
    is_empty = False

    # find the next empty cell
    for i in range(N):
        for j in range(N):
            if sudoku[i][j] == EMPTY:
                row = i
                col = j
                is_empty = True
                break
        if is_empty:
            break

    # if all cells are filled, the sudoku is solved
    if not is_empty:
        return True

    # try all possible numbers in the empty cell
    for num in range(1, 10):
        if isValid(sudoku, row, col, num):
            sudoku[row][col] = num

            if solveSudoku(sudoku):
                return True

            sudoku[row][col] = EMPTY

    return False

def generateSudoku():
    # fill the sudoku with random numbers
    sudoku = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            num = random.randint(1, 9)
            sudoku[i][j] = num
    return sudoku

sudoku = generateSudoku()

print("Sudoku puzzle:")
printSudoku(sudoku)

if solveSudoku(sudoku):
    print("\nSudoku solution:")
    printSudoku(sudoku)
else:
    print("Unable to solve sudoku")

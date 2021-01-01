def find_nextEmpty(puzzle):
    # finds the next row, col which is empty in the puzzle ie the place which is -1
    # returns (row,col) tuple or (None,None) if there is none such place
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None, None

def is_valid(guess,puzzle,row,col):
    # figures out whether the guess is valid or not
    # returns True if valid else False

    # if the guess exists in the row or column or 3x3 matrix then our guess is wrong

    # lets start with the row
    row_vals = puzzle[row] # row_vals is the list with all the values in the particular row
    if guess in row_vals:
        return False

    # now the columns
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col]) # col_vals is the list with all the values of the particular column
    if guess in col_vals:
        return False

    # now the 3x3 matrix
    # for this we need the start of the 3x3 matrix
    row_start = (row//3)*3
    col_start = (col//3)*3

    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c] == guess:
                return False

    # if all the checks are done means our guess is valid
    return True

def solveSudoku(puzzle):
    # solves the sudoku puzzle using backtracking technique
    # the puzzle is in the format of list in list where each inner list is a row in a sudoku
    # -1 represents the blank cell in the sudoku

    # step:1 Choose the place in the puzzle to make a guess
    row,col = find_nextEmpty(puzzle)

    #step:1.1 if there is nowhere left then we are done
    if row is None:
        return True

    # Step:2 if there is a place to put our guess, then make a guess between 1 and 9
    for guess in range(1,10):
        #step: 3 check if the guess is valid
        if is_valid(guess,puzzle,row,col):
            #step:3.1 if this is valid, then place the guess at the place
            puzzle[row][col]=guess
            #step:4 Recursively call the function
            if solveSudoku(puzzle):
                return True
        #step:5 if the guess didn't solve the puzzle then we nned to backtrack and try a new number
        puzzle[row][col] = -1 # reset the guess as it was not valid

    # step:6 if none of the number (guess) work then this puzzle doesn't have a solution
    return False

if __name__ == "__main__":
    sudoku = []
    size = int(input("Enter size of the sudoku, e.g. if it is 3x3 then enter only 3"))
    print("Enter the values, enter -1 in place of blank")
    for r in range(size):
        rows = []
        for c in range(size):
            rows.append(int(input()))
        sudoku.append(rows)

    print(sudoku)
    print(solveSudoku(sudoku))
    print(sudoku)


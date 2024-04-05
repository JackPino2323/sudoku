def solve(puzzle):
    
    
    row, col = find_next_space(puzzle)
    # if find_next_space cannot find an open space, returns the puzzle
    if row is None:
        return True
    
    for guess in range(1, 10):
        # tries every guess from 1-9
        # if guess is valid, updates the cell and calls solve() again
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            
            if solve(puzzle):
                return True
        
        # if the puzzle was not solved, resets the cell to -1 and tries next guess
        puzzle[row][col] = -1
            

def find_next_space(puzzle):
    # finds the next available space
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return (r, c)
            
    return (None, None)


def is_valid(puzzle, guess, row, col):
    # checks if the guess is in the row, column, or grid
    # if it is, returns false
    # otherwise returns true
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
        
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if guess == puzzle[r][c]:
                return False
    
    return True


def main():
    # accepts a 2D 9x9 list of values from 1-9 where empty spaces are represented with -1
    puzzle = [[ 3, -1, -1,   8, -1,  1,  -1, -1,  2],
              [ 2, -1,  1,  -1,  3, -1,   6, -1,  4],
              [-1, -1, -1,   2, -1,  4,  -1, -1, -1],
              
              [ 8, -1,  9,  -1, -1, -1,   1, -1,  6],
              [-1,  6, -1,  -1, -1, -1,  -1,  5, -1],
              [ 7, -1,  2,  -1, -1, -1,   4, -1,  9],
              
              [-1, -1, -1,   5, -1,  9,  -1, -1, -1],
              [ 9, -1,  4,  -1,  8, -1,   7, -1,  5],
              [ 6, -1, -1,   1, -1,  7,  -1, -1,  3]] 
    
    solve(puzzle)
    print(puzzle)
    
    
    
    
main()
    

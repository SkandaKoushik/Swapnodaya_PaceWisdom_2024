from pprint import pprint

def find_next_empty(p):
    
    for r in range(9):
        for c in range(9):
            if p[r][c] == -1:
                return r, c
            
    return None, None
            

def is_valid(p, guess, row, col):
    
    # Row Check
    row_vals = p[row]
    if guess in row_vals:
        return False
    
    # Col Check
    col_vals = [p[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # Square Check
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if p[r][c] == guess:
                return False
                
    return True



def slove_sudoku(p):
    
    row, col = find_next_empty(p)
    
    if row is None:
        return True
    
    for guess in range(1, 10):
        if is_valid(p, guess, row, col):
            p[row][col] = guess
            
            if slove_sudoku(p):
                return True
            
        p[row][col] = -1
        
    return False



board = [
    [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
    [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
    [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

    [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
    [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
    [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

    [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
    [6, 7, -1,   1, -1, 5,   -1, 4, -1],
    [1, -1, 9,   -1, -1, -1,   2, -1, -1]
]

slove_sudoku(board)
pprint(board)
        

    
import re
from board import Board

def play(dim_size=10, num_bombs=10):
    board = Board(dim_size, num_bombs)
    safe = True 

    while len(board.dug) < (board.dim_size ** 2 - num_bombs):
        print(board)     
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col >> "))  # '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        safe = board.dig(row, col)
        if not safe:
            break

    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
        print(board)
    else:
        print("SORRY GAME OVER :(")
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)
        

play()

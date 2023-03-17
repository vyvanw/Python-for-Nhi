COLUMN = 7
ROW = 6

def validate_input(prompt, valid_inputs):
    while True:
        user_input = input(prompt)
        if user_input in valid_inputs:
            return user_input
        else:
            print("Invalid input, please try again.")
            continue

def create_board():
    board = [[0 for _ in range(COLUMN)] for _ in range(ROW)]
    return board

def print_board(board):
    print("\n")
    print(f'{9*"="} Connect 4 {9*"="}', end="")
    print("\n")
    print(f'Player 1: x {5*" "} Player 2: O', end="")
    print("\n")
    for i in range(COLUMN):
        print(f"  {i + 1} ", end="")
    print("\n")
    for i in range(COLUMN):
        print(f" ---", end="")
    print("\n")

    for i in range(ROW):
        print('|', end='')
        for k in range(COLUMN):
            print(f" {board[i][k]} |", end="")
        print("\n")

def drop_piece(board, player, column):
    for i in range(ROW - 1, -1, -1):
        if board[i][int(column) - 1] == 0:
            board[i][int(column) - 1] = player
            return True
    return False

def execute_player_turn(player, board):
    while True:
        drop = drop_piece(board, player,validate_input(f"Player {player}, please enter the column you would like to drop your piece into: ",
                              ["1", "2", "3", "4", "5", "6", "7"]))
        if drop:
            print_board(board)
        else:
            print("That column is full, please try again.")
        break
        # if no break, the loop will keep going for each instance of execute_player_turn

board = create_board()
print_board(board)


execute_player_turn(1, board)
execute_player_turn(2, board)
execute_player_turn(1, board)
execute_player_turn(2, board)
execute_player_turn(1, board)
execute_player_turn(2, board)
execute_player_turn(1, board)
execute_player_turn(2, board)
execute_player_turn(1, board)
execute_player_turn(2, board)
execute_player_turn(1, board)
execute_player_turn(2, board)
execute_player_turn(1, board)
execute_player_turn(2, board)
execute_player_turn(1, board)
execute_player_turn(2, board)
#if use print(execute_player_turn(1, board)), it will print out the return value of the function, which is None
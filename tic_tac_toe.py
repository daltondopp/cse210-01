board = ["1","2","3",
        "4","5","6",
        "7","8","9"]

current_player = "X"
winner = None
game_running = True

def main():
    while game_running:
        print_board(board)
        player_input(board)
        check_win()
        check_tie(board) 
        switch_player()

def print_board(board):
    print(board[0]+ " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3]+ " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6]+ " | " + board[7] + " | " + board[8])

def player_input(board):
    inp = int(input(f"It is {current_player}'s turn.\nEnter a number 1-9: "))
    if inp >= 1 and inp <= 9:
        board[inp-1] = current_player
    else:
        print("That spot has already been chosen.")

def check_horizontle(board):
    global winner
    if board[0] == board[1] == board[2]  and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5]  and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8]  and board[6] != "-":
        winner = board[6]
        return True

def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def check_diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def check_tie(board):
    global game_running
    if "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9" not in board:
        print_board(board)
        print("It is a tie!")
        game_running = False

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else: current_player = "X"

def check_win():
    global game_running
    if check_diag(board) or check_horizontle(board) or check_row(board):
        print_board(board)
        print(f"The winner is {winner}!")
        game_running = False

if __name__ == '__main__':
    main()

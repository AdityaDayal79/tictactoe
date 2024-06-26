import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def check_draw(board):
    return all([cell != " " for row in board for cell in row])


def minimax(board, depth, is_maximizing):
    human = "X"
    ai = "O"

    if check_winner(board, ai):
        return 1
    if check_winner(board, human):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = ai
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = human
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score


def get_ai_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human = "X"
    ai = "O"

    print("Welcome to Tic-Tac-Toe!")
    print("You are X and the AI is O.")

    while True:
        print_board(board)
        move = input("Enter your move (row and column) as 'row,col': ")
        try:
            row, col = map(int, move.split(","))
            if board[row][col] != " ":
                print("Invalid move, cell already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column as numbers between 0 and 2, separated by a comma.")
            continue

        board[row][col] = human

        if check_winner(board, human):
            print_board(board)
            print("Congratulations! You win!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_move = get_ai_move(board)
        board[ai_move[0]][ai_move[1]] = ai

        if check_winner(board, ai):
            print_board(board)
            print("AI wins! Better luck next time.")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()










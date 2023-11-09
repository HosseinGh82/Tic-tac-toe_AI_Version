print("Hello everyone")
print("Welcome to Tic-tac-toe game:)\n")

board: list[list[str]] = [[" ", " ", " "],
                          [" ", " ", " "],
                          [" ", " ", " "]]


class Game:

    def __init__(self, board):
        self.board = board

    def printBoard(self):
        for i in range(5):
            for j in range(5):
                if i % 2 == 0 and j % 2 == 0:
                    print(self.board[i // 2][j // 2], end=" ")
                elif i % 2 == 1 and j % 2 == 0:
                    print("-", end=" ")
                else:
                    print("|", end=" ")
            print("")


def bestMove():
    move = (0, 0)
    bestScore = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = maxmin(board, 0, False)
                board[i][j] = " "
                if score > bestScore:
                    bestScore = score
                    move = (i, j)
    board[move[0]][move[1]] = "X"


def isFull(board1):
    for i in range(3):
        for j in range(3):
            if board1[i][j] == " ":
                return False
    return True


def checkWinner(board1):
    tempString3 = board1[0][0] + board1[1][1] + board1[2][2]
    tempString4 = board1[2][0] + board1[1][1] + board1[0][2]

    if tempString3 == "XXX" or tempString4 == "XXX":
        return 1
    elif tempString3 == "OOO" or tempString4 == "OOO":
        return -1

    for i in range(3):
        tempString1 = ""
        tempString2 = ""
        for j in range(3):
            tempString1 += board1[i][j]
            tempString2 += board1[j][i]
        if tempString1 == "XXX" or tempString2 == "XXX":
            return 1
        elif tempString1 == "OOO" or tempString2 == "OOO":
            return -1
        elif isFull(board):
            return 0
    return 2


def maxmin(board1, depth, isMaximizing):
    result = checkWinner(board1)
    if result != 2:
        return result

    if isMaximizing:
        bestScore = float('-inf')
        for i in range(3):
            for j in range(3):
                if board1[i][j] == " ":
                    board1[i][j] = "X"
                    score = maxmin(board1, depth + 1, False)
                    board1[i][j] = " "
                    bestScore = max(score, bestScore)
        return bestScore

    else:
        bestScore = float('inf')
        for i in range(3):
            for j in range(3):
                if board1[i][j] == " ":
                    board1[i][j] = "O"
                    score = maxmin(board1, depth + 1, True)
                    board1[i][j] = " "
                    bestScore = min(score, bestScore)
        return bestScore


game = Game(board)

turn = 1
while True:

    game.printBoard()
    print("\n")

    result = checkWinner(board)
    if result != 2:
        if result == 1:
            print("AI IS WINNER!")
        elif result == -1:
            print("YOU ARE WINNER!")
        else:
            print("DRAW")
        break

    if turn == 1:
        bestMove()
        turn = 0
    else:
        print("Enter Your choice", ": ", end="")
        number = int(input())
        if board[(number - 1) // 3][(number - 1) % 3] != " ":
            continue
        else:
            board[(number - 1) // 3][(number - 1) % 3] = "O"
            turn = 1

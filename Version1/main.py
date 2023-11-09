from typing import List

print("Hello everyone")
print("Welcome to Tic-tac-toe game:)\n")

board: list[list[str]] = [['1', '2', '3'],
                          ['4', '5', '6'],
                          ['7', '8', '9']]

scores = {1: "X", -1: "O", 0: "tie"}


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


def checkWinner(board):
    tempString3 = board[0][0] + board[1][1] + board[2][2]
    tempString4 = board[0][2] + board[1][1] + board[2][0]

    if tempString3 == "XXX" or tempString4 == "XXX":
        return 1
    elif tempString3 == "XXX" or tempString4 == "XXX":
        return -1

    for i in range(3):
        tempString1 = ""
        tempString2 = ""
        for j in range(3):
            tempString1 += board[i][j]
            tempString2 += board[j][i]
        if tempString1 == "XXX" or tempString2 == "XXX":
            return 1
        elif tempString1 == "OOO" or tempString2 == "OOO":
            return -1
        elif i == 2 and j == 2:
            return 0
    return 2


def maxmin(board1, depth, isMaximizing):
    result = checkWinner(board1)
    if result != 2:
        return result

    if isMaximizing:
        bestScore = -2
        for i in range(3):
            for j in range(3):
                if board1[i][j] != "O" or board1[i][j] != "X":
                    board1[i][j] = "X"
                    score = maxmin(board1, depth + 1, False)
                    board1[i][j] = (i * 3) + j + 1
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 2
        for i in range(3):
            for j in range(3):
                if board1[i][j] != "O" or board1[i][j] != "X":
                    board1[i][j] = "O"
                    score = maxmin(board1, depth + 1, True)
                    board1[i][j] = (i * 3) + j + 1
                    bestScore = min(score, bestScore)
        return bestScore


game = Game(board)
turn = 1
while True:
    game.printBoard()

    if turn == 1:
        maxmin(board, 1, True)
    else:
        print("Enter Your choice ", ":", end="")
        x = int(input())
        y = int(input())

        board[x][y] = "O"

        if checkWinner(board) != 2:
            break

    print("\n")

# print(maxmin(board, 1, True))




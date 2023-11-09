
print("Hello everyone")
print("Welcome to Tic-tac-toe game:)\n")

board: list[list[int]] = [[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]]


class Game:

    def __init__(self, firstPlayer, board):
        self.firstPlayer = firstPlayer
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


game = Game(1, board)



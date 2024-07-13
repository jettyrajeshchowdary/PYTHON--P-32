import random

class CarromGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.players = [player1, player2]
        self.board = Board()
        self.current_player = random.choice(self.players)
        self.winner = None

    def play(self):
        while not self.winner:
            print(f"It's {self.current_player}'s turn.")
            shot = self.current_player.take_shot(self.board)
            if shot == "foul":
                print(f"{self.current_player} fouled!")
                self.switch_player()
            elif shot == "win":
                self.winner = self.current_player
                print(f"{self.current_player} wins!")
            else:
                self.board.update(shot)
                self.switch_player()

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

class Board:
    def __init__(self):
        self.pockets = {"red": [], "white": [], "black": []}
        self.center = {"red": False, "white": False, "black": False}

    def update(self, shot):
        if shot in self.pockets:
            self.pockets[shot].append(1)
        elif shot == "center":
            self.center[self.current_player.color] = True

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def take_shot(self, board):
        pass

class HumanPlayer(Player):
    def take_shot(self, board):
        pass

class ComputerPlayer(Player):
    def take_shot(self, board):
        pass

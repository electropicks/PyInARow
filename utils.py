import sys
from termcolor import colored
import numpy as np

color_to_code = {"white": None, "red": True, "yellow": False}
code_to_color = {None: "white", True: "red", False: "yellow"}

def printf(string):
    sys.stdout.write(string)

class Game:
    def __init__(self, p1, p2, rows, cols):
        self.turn = True
        self.p1 = p1
        self.p2 = p2
        self.rows = rows
        self.cols = cols
        self.grid = [[None] * cols for i in range(cols)]
        draw_board(self)
    def play(self):
        while True:
            try:
                choice = int(input((self.p1 if self.turn else self.p2) + " pick a column for your next piece: "))
                if choice not in range(1, self.cols + 1):
                    print("Not a valid entry, try again")
                    continue
                elif self.rows == len(self.grid[choice-1]):
                    print("This column is full, pick a different one")
                    continue
                break
            except:
                    print("Not a valid entry, try again")
        choice -= 1
        #choice is a number [0, 6]
        col = 0
        curr = self.grid[choice][col]
        while curr is not None:
            col += 1
            curr = self.grid[choice][col]
        self.grid[choice][col] = self.turn
        self.turn = not self.turn
        draw_board(self)



def draw_board(game):
    printf("\n")
    for row in range(game.rows - 1, -1, -1):
        for col in range(game.cols):
            color = code_to_color[game.grid[col][row]]
            printf(colored("|", "blue") + colored("⦿", color))
        print(colored("|", "blue"))
    for col in range(game.cols):
        printf(" " + str(col + 1))
    printf("\n")
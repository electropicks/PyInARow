import sys
from termcolor import colored

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
        self.over = False
        draw_board(self)
    def play(self):
        all_full = True
        for i in range(self.cols):
            if count_col(self, i) < len(self.grid[i]):
                all_full = False
        if all_full:
            self.over = True
            draw_board(self)
            return
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

        self.grid[choice][count_col(self, choice)] = self.turn
        if (row_test(self, choice, count_col(self, choice) - 1)) or\
        (column_test(self, choice, count_col(self, choice) - 1)) or\
        (up_diag_test(self, choice, count_col(self, choice) - 1)) or\
        (down_diag_test(self, choice, count_col(self, choice) - 1)):
            self.over = True
            draw_board(self)
            return
        self.turn = not self.turn
        draw_board(self)

def count_col(game, col):
    curr = game.grid[col][0]
    count = 0
    while curr is not None:
        count += 1
        curr = game.grid[col][count]
    return count

def row_test(game, col, row):
    countR = 0
    #to the right
    while (col + 1 + countR) in range(game.cols) and game.grid[col + 1 + countR][row] == game.grid[col][row]:
        countR += 1
    #to the left
    countL = 0
    while (col - 1 + countL) in range(game.cols) and game.grid[col - 1 + countL][row] == game.grid[col][row]:
        countL -= 1
    countL = abs(countL)
    if countL + countR >= 3:
        return True
    else:
        return False

def column_test(game, col, row):
    count_up = 0
    #to the right
    while (row + 1 + count_up) in range(game.rows) and game.grid[col][row + 1 + count_up] == game.grid[col][row]:
        count_up += 1
    #to the left
    count_down = 0
    while (row - 1 + count_down) in range(game.rows) and game.grid[col][row - 1 + count_down] == game.grid[col][row]:
        count_down -= 1
    count_down = abs(count_down)
    if count_down + count_up >= 3:
        return True
    else:
        return False

def up_diag_test(game, col, row):
    count_up = 0
    #to the right
    while col + 1 + count_up in range(game.cols) and row + 1 + count_up in range(game.rows) and\
    game.grid[col + 1 + count_up][row + 1 + count_up] == game.grid[col][row]:
        count_up += 1
    #to the left
    count_down = 0
    while (row - 1 + count_down) in range(game.rows) and (col - 1 + count_down) in range(game.cols) and\
    game.grid[col - 1 + count_down][row - 1 + count_down] == game.grid[col][row]:
        count_down -= 1
    count_down = abs(count_down)
    if count_down + count_up >= 3:
        return True
    else:
        return False

def down_diag_test(game, col, row):
    count_up = 0
    #to the right
    while (col - 1 - count_up) in range(game.cols) and (row + 1 + count_up) in range(game.rows) and\
    game.grid[col - 1 - count_up][row + 1 + count_up] == game.grid[col][row]:
        count_up += 1
    #to the left
    count_down = 0
    while (col + 1 - count_down) in range(game.cols) and (row - 1 + count_down) in range(game.cols) and\
    game.grid[col + 1 - count_down][row - 1 + count_down] == game.grid[col][row]:
        count_down -= 1
    count_down = abs(count_down)
    if count_down + count_up >= 3:
        return True
    else:
        return False

def draw_board(game):
    printf("\n")
    for row in range(game.rows - 1, -1, -1):
        for col in range(game.cols):
            color = code_to_color[game.grid[col][row]]
            printf(colored("|", "blue") + (colored("○", "blue") if color == "white" else colored("◉", color)))
        print(colored("|", "blue"))
    for col in range(game.cols):
        printf(" " + str(col + 1))
    printf("\n")
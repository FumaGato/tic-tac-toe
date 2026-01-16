import os
import sys

rahhh = r"""
⣿⣿⣿⢟⣤⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣋⣥⢹⣿
⣿⣿⢋⣾⣿⣿⣎⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣴⣿⣿⣇⢻
⣿⡏⣾⣿⣿⣿⣿⣷⣌⠻⣿⣇⢶⣶⣭⣙⡻⢿⣿⣿⣿⡿⢋⣴⣿⣿⣿⣿⣿⡜
⣿⢣⣿⣿⣿⣿⣿⣿⣿⣷⡙⢿⡜⢿⣿⣿⣿⣶⣝⠿⠟⣵⣿⣿⣿⣿⣿⣿⣿⡇
⣿⢸⣿⣿⣿⣿⣿⣿⣿⡿⢟⣠⣵⣶⣾⣿⣿⣿⣿⣷⣜⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⢸⣿⣿⣿⣿⣿⣿⣿⣥⣭⣭⣭⣭⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢹
⣿⣷⡹⣿⣿⡟⠛⠛⠛⠛⠛⠻⢿⣿⣿⣿⣿⡟⠛⠛⠉⣭⣍⢩⣽⣿⣿⡿⢣⣿
⠿⣿⣷⡙⣿⡟⢸⣿⣟⠀⠀⠀⣿⣿⣿⣿⣿⠁⠀⠀⠀⣿⣿⡎⣿⣿⠟⠑⠛⢿
⡌⢶⣶⣦⣾⡇⢿⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣇⠀⠀⢸⣿⣿⡇⣿⣿⣿⡿⢋⣾
⣿⣦⣝⢻⡿⢿⣼⣿⣿⣦⣤⣼⣿⣭⣽⣿⣿⣿⣷⣾⣿⡿⠛⠟⣿⣿⡋⢴⣿⣿
⣿⣿⢃⣿⣷⣥⣴⣾⣿⣿⣿⡿⢿⡿⢛⠛⠟⣛⣿⣿⣿⣷⣧⣾⣿⣿⣿⣮⢻⣿
⣿⣇⣚⣛⣛⣛⠻⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣫⣭⣽⣭⣭⣤⣿
⣿⣿⣿⣿⣿⣿⣿⣦⡨⣭⣛⣛⣿⣿⣿⣿⣿⣿⣿⣷⡆⢾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⡬⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡜⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡏⠘⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢸⣿⣿⣿⣿⣿
"""


class Grid:
    def __init__(self, name):
        self.name = name
        self.contain = " "
        self.is_marked = False

    def mark(self, player):
        self.contain = player.mark
        self.is_marked = True

    def __repr__(self):
        return self.contain


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.win = False

    def __repr__(self):
        return self.mark


class WinCon:
    def __init__(self, grid1, grid2, grid3):
        self.grid1 = grid1
        self.grid2 = grid2
        self.grid3 = grid3

    def check_win(self):
        if self.grid1.is_marked and self.grid2.is_marked and self.grid3.is_marked:
            if self.grid1.contain == self.grid2.contain == self.grid3.contain:
                return 1
            else:
                return 2
        else:
            return 0


a1 = Grid("a1")
a2 = Grid("a2")
a3 = Grid("a3")
b1 = Grid("b1")
b2 = Grid("b2")
b3 = Grid("b3")
c1 = Grid("c1")
c2 = Grid("c2")
c3 = Grid("c3")

grids = [a1, a2, a3, b1, b2, b3, c1, c2, c3]

p1 = Player("P1", "X")
p2 = Player("P2", "O")

row1 = WinCon(a1, b1, c1)
row2 = WinCon(a2, b2, c2)
row3 = WinCon(a3, b3, c3)
col1 = WinCon(a1, a2, a3)
col2 = WinCon(b1, b2, b3)
col3 = WinCon(c1, c2, c3)
dia1 = WinCon(a1, b2, c3)
dia2 = WinCon(a3, b2, c1)

win_cons = [
    row1,
    row2,
    row3,
    col1,
    col2,
    col3,
    dia1,
    dia2
]


def clear_terminal():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix-like systems (Linux, macOS)
    else:
        _ = os.system('clear')


def tic_tac_toe(player1, player2):
    for grid in grids:
        grid.contain = " "
        grid.is_marked = False
    player1.win = False
    player2.win = False
    clear_terminal()
    while True:
        print_grid()
        start_turn(player1)
        clear_terminal()
        if check_win(player1) == 1:
            break
        if check_draw() == True:
            break
        print_grid()
        start_turn(player2)
        clear_terminal()
        if check_win(player2) == 1:
            break
        if check_draw() == True:
            break
    if player1.win:
        win(player1)
    if player2.win:
        win(player2)
    if check_draw() == True:
        draw()


def print_grid():
    print(rahhh)
    print(f"   A   B   C")
    print(f"1 |{a1}| |{b1}| |{c1}|")
    print(f"2 |{a2}| |{b2}| |{c2}|")
    print(f"3 |{a3}| |{b3}| |{c3}|")


def start_turn(player):
    done = False
    while done == False:
        select_grid = input(f"[{player}] {player.name} > ").lower()
        for grid in grids:
            if grid.name == select_grid[:2]:
                if grid.is_marked == False:
                    grid.mark(player)
                    done = True


def check_win(player):
    for con in win_cons:
        if con.check_win() == True:
            player.win = True
            return True


def check_draw():
    not_win_con = 0
    for con in win_cons:
        if con.check_win() == 2:
            not_win_con += 1
    if not_win_con == 8:
        return True


def win(player):
    print(rahhh)
    print(f"   A   B   C")
    print(f"1 |{a1}| |{b1}| |{c1}|")
    print(f"2 |{a2}| |{b2}| |{c2}|")
    print(f"3 |{a3}| |{b3}| |{c3}|")
    print(f"{player.name} ({player.mark}) WIN!")
    print("Play again? (y/n)")
    choice = input("> ")
    if choice == "y":
        tic_tac_toe(p1, p2)
    else:
        pass


def draw():
    print(rahhh)
    print(f"   A   B   C")
    print(f"1 |{a1}| |{b1}| |{c1}|")
    print(f"2 |{a2}| |{b2}| |{c2}|")
    print(f"3 |{a3}| |{b3}| |{c3}|")
    print("DRAW.")
    print("Play again? (y/n)")
    choice = input("> ")
    if choice == "y":
        tic_tac_toe(p1, p2)
    else:
        sys.exit()


tic_tac_toe(p1, p2)

# I'm just an amateur programmer

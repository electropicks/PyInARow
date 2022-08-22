from utils import *

if __name__ == "__main__":
    print("""Hello! Welcome to Py in a Row, the game where you have to align about 3.14 pieces of your color before your opponent does so with theirs.""")
    print("""
    ██████╗░██╗░░░██╗██╗███╗░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
    ██╔══██╗╚██╗░██╔╝██║████╗░██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
    ██████╔╝░╚████╔╝░██║██╔██╗██║███████║██████╔╝██║░░██║░╚██╗████╗██╔╝
    ██╔═══╝░░░╚██╔╝░░██║██║╚████║██╔══██║██╔══██╗██║░░██║░░████╔═████║░
    ██║░░░░░░░░██║░░░██║██║░╚███║██║░░██║██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░
    ╚═╝░░░░░░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░""")
    #setup done

    #game begins
    p1 = input("Player 1, input your name: ").title()
    p1 = p1[:min(len(p1), 10)]
    p2 = input("Player 2, input your name: ").title()
    p2 = p2[:min(len(p2), 10)]


    game = Game(p1, p2, rows=6, cols=7)
    while not game.over:
        game.play()
    print(game.p1 if game.turn else game.p2, "got more than py (3.14) in a row! Thanks for playing!")


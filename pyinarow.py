from re import L
from matplotlib.pyplot import draw
from utils import *
from termcolor import colored

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
p1 = input("Player 1, input your name: ")
p1 = p1[:min(len(p1), 10)]
p2 = input("Player 2, input your name: ")
p2 = p2[:min(len(p2), 10)]


game = Game(p1, p2, rows=6, cols=7)
for i in range(10):
    game.play()


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

#print empty board
num_of_rows = 6
num_of_cols = 7
    #setup top edge
for col in range(num_of_cols*2 + 1):
    printf(colored("-", "blue"))
printf("\n")

    #setup board itself
for row in range(num_of_rows+1):
    color = "grey"
    for col in range(num_of_cols):
        printf(colored("|", "blue") + colored("◉", color), )
    if col != 0:
        print(colored("|", "blue"))

    #setup bottom edge
for col in range(num_of_cols*2 + 1):
    printf(colored("-", "blue"))
printf("\n ")
    #setup line numbers
for col in range(num_of_cols):
    print(str(col) + " ", end = '')


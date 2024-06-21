from random import randint
import os

os.system("cls")

print("Humpyang Game")
#0 for unfold and 1 for fold
#Removed the convert to text function for optimzation purposes
#Using only 0 and 1 to determine the output
p1 = int(input("Input 0 or 1: "))
c1 = randint(0,1)
c2 = randint(0,1)

if (p1 and c1 and c2 == 0) and (p1 and c1 and c2 == 1):
    print("Tie!")
elif p1 == 0 and c1 == 1 and c2 == 1 or p1 == 1 and c1 == 0 and c2 == 0:
    print("Player 1 wins!")
elif c1 == 0 and p1 == 1 and c2 == 1 or p1 == 1 and p1 == 0 and c2 == 0:
    print("Computer 1 wins!")
elif c2 == 0 and c1 == 1 and p1 == 1 or p1 == 1 and c1 == 0 and p1 == 0:
    print("Computer 2 wins!")


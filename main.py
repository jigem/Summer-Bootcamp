from random import randint
import os

os.system("cls")

print("Humpyang Game")
p1 = int(input("Input 0 or 1: "))
c1 = randint(0,1)
c2 = randint(0,1)
#Choices Reveal
if p1 == 1:
    p1 = "UNFOLD"
    print("Player 1 UNFOLD!")
elif p1 == 0:
    p1 = "FOLD"
    print("Player 1 FOLD!")
if c1 == 1:
    c1 = "UNFOLD"
    print("Computer 1 UNFOLD!")
elif c1 == 0:
    c1 = "FOLD"
    print("Computer 1 FOLD!")
if c2 == 1:
    c2 = "UNFOLD"
    print("Computer 2 UNFOLD!")
elif c2 == 0:
    c2 = "FOLD"
    print("Computer 2 FOLD!")

if p1 == "FOLD" and c1 == "FOLD" and c2 == "FOLD" or p1 == "UNFOLD" and c1 == "UNFOLD" and c2 == "UNFOLD":
    print("Tie!")
elif p1 == "UNFOLD" and c1 == "FOLD" and c2 == "FOLD" or p1 == "FOLD" and c1 == "UNFOLD" and c2 == "UNFOLD":
    print("Player 1 wins!")
elif c1 == "UNFOLD" and p1 == "FOLD" and c2 == "FOLD" or c1 == "FOLD" and p1 == "UNFOLD" and c2 == "UNFOLD":
    print("Computer 1 wins!")
elif c2 == "UNFOLD" and c1 == "FOLD" and p1 == "FOLD" or c2 == "FOLD" and c1 == "UNFOLD" and p1 == "UNFOLD":
    print("Computer 2 wins!")


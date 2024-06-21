from random import randint
import os 

os.system("cls")

#Optimized 6/21/24, minimized the forloop in bet and result

#Input the bet of the user
bet = [int(input(f"Enter bet {i+1} (0-9): ")) for i in range(3)]
print("Your bets:", bet)

#Generate random numbers for the result
# result = [randint(0, 9) for _ in range(3)]
# print("Result:", result)
result = [1,2,3]

#Statements to determine the outcome for each, this part stays the same as i have not seen any better code
if bet == result:
    print("You win! Perfect Combination!")
elif sorted(bet) == sorted(result):
    print("You Partially Win!")
else:
    print("You Lose")

from random import randint

bet = []

for i in range(3):
    bets = int(input("Enter your bets (0-9): "))
    bet.append(bets)
    
print("Your bets:", bet)

result = []

for i in range(3):
    results = randint(0, 9)
    result.append(results)
    
print("Result:", result)

if bet == result:
    print("You win! Perfect Combination!")
elif sorted(bet) == sorted(result):
    print("You Partially Win!")
else:
    print("You Lose")

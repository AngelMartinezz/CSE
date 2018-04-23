import random

money = 15

while money > 0:
    dice1 = random.randint(1, 6)
    print(dice1)

    dice2 = random.randint(1, 6)
    print(dice2)

    total = dice1 + dice2
    print(total)

    if total == 7:
        print("You win this round.")
    else:
        money -= 1


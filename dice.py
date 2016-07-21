import random
print("""
        Dice Simulator
 Do you want to roll the dice?
 """)
min = 1
max = 6
rollAgain = "yes"
while rollAgain == "yes" or rollAgain == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
    print (random.randint(min, max))
    rollAgain =input("Roll the dices again?")


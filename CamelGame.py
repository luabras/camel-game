import random

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and outrun the natives.")

print("\nIf your thirst level is greater than 6, you die.")
print("If your camel's level of tiredness is greater than 8, it dies and you will be caught.")

done = False
mTraveled = 0
thirst = 0
camTired = 0
nativTraveled = -20
nativDistance = 0
canteen = 5
oasisChance = 0

while not done:

    nativDistance = mTraveled - nativTraveled
    
    print("\nA. Drink from your canteen. ")
    print("B. Ahead moderate speed. ")
    print("C. Ahead full speed. ")
    print("D. Stop and rest. ")
    print("E. Status check. ")
    print("Q. Quit. \n")    
    
    choice = input("Your choice? ")

    if choice.upper() == "Q":
        done = True
        
    elif choice.upper() == "E":
        print("\nMiles traveled: ", mTraveled)
        print("Drinks in canteen: ", canteen)
        print("The natives are", nativDistance, "miles behind you.")
        print("The camel's level of tiredness is: ", camTired)
        print("Your thirst level is: ", thirst)
        
    elif choice.upper() == "D":
        camTired = 0
        print("\nThe camel is happy.")
        nativTraveled += random.randrange(8, 17)
        
    elif choice.upper() == "C":
        mTraveled += random.randrange(10, 21)
        print("\nMiles traveled: ", mTraveled)
        thirst = thirst + 1
        camTired += random.randrange(1, 3)
        nativTraveled += random.randrange(8, 17)
        oasisChance = random.randrange(1,51)
    
    elif choice.upper() == "B":
        mTraveled += random.randrange(5, 13)
        print("\nMiles traveled: ", mTraveled)
        thirst = thirst + 1
        camTired = camTired + 1
        nativTraveled += random.randrange(8, 17)
        oasisChance = random.randrange(1,51)
        
    elif choice.upper() == "A":
        if canteen > 0:
            canteen = canteen - 1
            thirst = 0
        else:
            print("\nThe canteen is empty.")

    if oasisChance == 50:
        print("\nYou have found and Oasis! Now your canteen is full, you feel no thirst and your camel is well rested!")
        canteen = 5
        thirst = 0
        camTired = 0

    if (thirst > 4 and thirst <= 6 and not done):
        print("\nYou are thirsty!")
    elif thirst > 6:
        print("\nYou died of thirst! :( ")
        done = True

    if (camTired > 5 and camTired <= 8 and not done):
        print("\nYour camel is getting tired...")
    elif camTired > 8 and not done:
        print("\nYour camel is dead!!!")
        done = True

    if nativTraveled >= mTraveled:
        print("\nYou were caught by the natives!")
        done = True
        
    if nativDistance <= 15 and not done:
        print("\nThe natives are getting close!")

    if mTraveled > 500 and not done:
        print("\nYou have escaped!")
        done = True
        
print("\nDone.")

import random
import time

print("Welcome to the GUESS THE NUMBER game!")
time.sleep(2)
print("Your task is simple...")
time.sleep(2)
print("Just guess the number...")
time.sleep(2)
print("Which I think!")
time.sleep(2)
input("When you are ready press ENTER")
time.sleep(1)

play = True

while play:
    nrstart = input("What number should I start from: ")
    time.sleep(1)
    nrstop = input("At what number should I stop: ")
    time.sleep(1)
    print("All right! I think the number...")
    time.sleep(1)
    print("from " + nrstart + " to " + nrstop + "\n")
    time.sleep(1)
    takes = input("In how many attempts can you do it: \n")

    pc = random.randint(int(nrstart),int(nrstop))
    count = 0
    player = 0

    time.sleep(1)

    while pc != player:
        player = int(input("Guess the number from" + nrstart + " to " + nrstop + ": "))
        count += 1
        if pc > player:
            time.sleep(1)
            print("more\n")
        if pc < player:
            time.sleep(1)
            print("less\n")

    time.sleep(1)        
    print("CONGRATULATIONS, you've guessed!")
    time.sleep(1)
    print("The number of attempts required to guess is? " + str(count) + "\n")
    time.sleep(1)

    if int(count) <= int(takes):
        print("Excellent, you managed to guess my number pretty quickly.\n")
    else:
        print("Unfortunately, it took you too many tries.\n")

    again = str(input("Do you want to play again? Y/N\n"))

    if again == "y" or again == "Y":
        play = True
    else:
        play = False

input("Thank you for playing my game. Have a nice day...")

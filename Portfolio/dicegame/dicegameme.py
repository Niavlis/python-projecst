import random
import time
import statistics
results = []

play = "y"

while play == "y": 
    print ("You want to gamble?????")
    time.sleep(0.5)
    print ("Choose ")
    time.sleep(0.5)
    print ("Do you want to guess the average    1   ")
    time.sleep(0.5)
    print ("or do you want to guess the mode      2   ")
    time.sleep(0.5)
    print ("lastly would u like to guess a single number     3    ")
    time.sleep(0.5)
    print ("Choose 1, 2 or 3 ")
    what = int(input())

    if what == 1:
        print ("How many dice")
        amount = int(input())

        for i in range(amount):
            part =  random.randint(1, 6)
            results.append(part)

        fRes = sum(results) / amount
        fRes = int(fRes)  

        print("Now you have to choose")
        print("its a full number")
        print("Guess")
        guess = int(input())

        if guess == fRes:
            time.sleep(0.5)
            print ("Good job")
            time.sleep(0.5)
            print ("Want to play again")
            time.sleep(0.5)
            print ("y for yes, n for no")
            play = input()
            if play == "y":
                continue
            else:
                print("i bet ill see you again")
                break
        else:
            print ("oops youre wrong")
            time.sleep(0.4)
            print ("Haha i win")
            time.sleep(0.4)
            print ("Want to play again")
            time.sleep(0.5)
            print ("y for yes, n for no")
            play = input()
            if play == "y":
                continue
            else:
                print("i bet ill see you again")
                break
            
    if what == 2:
        print("The mode is the most occuring number in a series of numbers")
        time.sleep (1)
        print("how many numbers are there in the sequence???? ")
        amount = int(input())
        print("What is the lowest possible num? ")
        numl = int(input())
        print("What is the highest possible num? ")
        numh = int(input())
        for i in range(amount): 
            part = random.randint(numl, numh)
            results.append(part)
        
        modelist = statistics.mode(results)
        time.sleep(2)
        print("tell me what is the mode")
        guess = int(input())
        time.sleep(1.5)
        if guess == modelist:
            time.sleep(0.5)
            print ("Good job")
            time.sleep(0.5)
            print ("Want to play again")
            time.sleep(0.5)
            print ("y for yes, n for no")
            play = input()
            if play == "y":
                continue
            else:
                print("i bet ill see you again")
                break
        else:
            print ("oops youre wrong")
            time.sleep(0.4)
            print ("Haha i win")
            time.sleep(0.4)
            print ("Want to play again")
            time.sleep(0.5)
            print ("y for yes, n for no")
            play = input()
            if play == "y":
                continue
            else:
                print("i bet ill see you again")
                break
    if what == 3:
        print ("this is a simple guess")
        print ("between 1 and 6 ")
        print ("choose ")
        guess = int(input())
        if guess == random.randint(1,6):
            time.sleep(0.5)
            print ("Good job")
            time.sleep(0.5)
            print ("Want to play again")
            time.sleep(0.5)
            print ("y for yes, n for no")
            play = input()
            if play == "y":
                continue
            else:
                print("i bet ill see you again")
                break
        else:
            print ("oops youre wrong")
            time.sleep(0.4)
            print ("Haha i win")
            time.sleep(0.4)
            print ("Want to play again")
            time.sleep(0.5)
            print ("y for yes, n for no")
            play = input()
            if play == "y":
                continue
            else:
                print("i bet ill see you again")
                break

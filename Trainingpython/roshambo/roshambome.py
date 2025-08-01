import random
import time

play = "y"

while play == "y":
    hand = random.randint(1,3)
    print ( "Rock Paper Scissors")
    time.sleep(1)
    print ("Choose 1 2 or 3")
    hand2 = int(input())
    
    if hand == 1 and hand2 == 3:
        win = "l"
    if hand == 1 and hand2 == 2:
        win = "w"
    if hand == 1 and hand2 == 1:
        win = "t"
    
    if hand == 2 and hand2 == 3:
        win = "w"
    if hand == 2 and hand2 == 2:
        win = "t"
    if hand == 2 and hand2 == 1:
        win = "l"
    
    if hand == 3 and hand2 == 3:
        win = "t"
    if hand == 3 and hand2 == 2:
        win = "l"
    if hand == 3 and hand2 == 1:
        win = "w"
    
    if hand == 1:
        hand = "Stone"
    elif hand == 2:
        hand = "Paper"
    elif hand == 3:
        hand = "Scissors"
    
    if hand2 == 1:
        hand2 = "Stone"
    elif hand2 == 2:
        hand2 = "Paper"
    elif hand2 == 3:
        hand2 = "Scissors"
    
    if win == "w":
        time.sleep(1)
        print ("The opponent had ", hand, " You win")
        time.sleep(1)
        print ("Would u like to play again?")
        time.sleep(1)
        print("y for yes, n for no")
        play = input()
        if play == "y":
            time.sleep(1)
            continue
        else:
            break
    
    if win == "t":
        time.sleep(1)
        print ("The opponent had ", hand, " Its a tie")
        time.sleep(1)
        print ("Would u like to play again?")
        time.sleep(1)
        print("y for yes, n for no")
        play = input()
        if play == "y":
            time.sleep(1)
            continue
        else:
            break
    
    if win == "l":
        time.sleep(1)
        print ("The opponent had ", hand, " You lose ")
        time.sleep(1)
        print ("Would u like to play again?")
        time.sleep(1)
        print("y for yes, n for no")
        play = input()
        if play == "y":
            time.sleep(1)
            continue
        else:
            break
    


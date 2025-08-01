import time 
import sys
redo = "Y"


while redo == "Y": 
    print ("you wanna try calculation")

# asks the questions
    type = input ("choose 1, * , / , +. - ")
    num1 = input("Whats the first number?  ")
    num2 = input("Whats the second number?????  ")
# makes the nums integers
    num1 = int(num1)
    num2 = int(num2)
# decides what to do

    if type == "*":
        result = num1 * num2
    elif type == "/":
        result = num1 / num2
    elif type == "+":
        result = num1 + num2
    elif type == "-":
        result = num1 - num2


    if type not in["*","/","+", "-"]:
        time.sleep(0.5)
        print ("You fool")
        time.sleep(0.5)
        print ("You doodoofart")
        time.sleep(0.5)
        print ("there is no way to calculate a ", type )
        print("Want to play again?")
        time.sleep(0.5)
        print("Y for Yes and N for No ")
        time.sleep(0.5)
        print("Y or N")
        redo = input()
        if redo == "Y":
            continue
        else:
            sys.exit()
    if type in ["*","/","+", "-"]:
   
        guees = input("So you want to use me??????????  well then guess ")
        guees = int(guees)
    if guees == result:
          time.sleep(0.5)
          print ("Smart ass")
          time.sleep(0.5)
          print ("Good job you won")
          time.sleep(0.5)
          print ("Next time you will lose")
          time.sleep(0.5)
          print ("I can feel it")
          time.sleep(0.5)
          print ("Wanna go again.")
          time.sleep(0.5)
          print ("I know i can beat you.")
          time.sleep(0.5)
          print("Y for Yes and N for No ")
          print("Y or N")
          redo= input()
    else:
        print("Hahaha you lose.")
        time.sleep(0.5)
        print("Want to play again?")
        time.sleep(0.5)
        print("I feel like you will win")
        time.sleep(0.5)
        print("Y for Yes and N for No ")
        time.sleep(0.5)
        print("Y or N")
        redo = input()
    if redo == "Y":
        continue
    else:
        sys.exit

    
        



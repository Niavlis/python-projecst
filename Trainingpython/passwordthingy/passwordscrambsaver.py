import json
import random
import sys
chars = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*"
passlist = []
password = ""
c = 1
cycle = ""
while c == 1:
    print ("wahat do u want to do")
    print ( "Look at a password    1 ")
    print (" or create a new one    2 ")
    what = int(input())
    if what == 2:
            
        print("for what application is this password")
        fname = input()
        print ("how many chars")

        amount = int(input())
        for i in range(amount):
                ranchar = random.choice(chars)
                ranchar2 = random.choice(chars)
                password = ranchar + ranchar2 + password

        print (password)
        file_path = "Portfolio/passwordthingy/passfor"

        file_path = file_path + fname + ".json"

        with open(file_path, "w") as save:
            json.dump(password, save)
        
    elif what == 1:
        print( "what is the name of the application u need it for")
        fname = input()
        file_path = "Portfolio/passwordthingy/passfor"    
        file_path = file_path + fname + "json"
        try:
            with open(file_path, "r") as load:
                passwordloaded = json.load(load)
        except FileNotFoundError:
            print("Error: 'data.json' not found.")

        except json.JSONDecodeError:
            print("Error: Invalid JSON format in 'data.json'.")
        print("Your password is")
        print(passwordloaded)
        cycle = input("Press enter to continue Press n to quit" )
    if cycle == "n": 
        sys.exit
    else:
        continue


         
    




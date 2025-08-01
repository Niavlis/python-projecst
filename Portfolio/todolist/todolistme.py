import json 
import time
import sys

clist = 0


list = []
datafile = "Portfolio/todolist/save.json"
try: 
    with open(datafile, "r") as l:
        list = json.load(l)

except FileNotFoundError:
    print("Error: 'data.json' not found.")

except json.JSONDecodeError:
    print("Error: Invalid JSON format in 'data.json'.") 


while clist == 0:
    print ("What would u like to do?")
    print ("Look at the list? Enter 1")
    print ("Add something to the list? Enter 2")
    print ("Remove something from the list Enter 3")
    print("Or exit the program with a save Enter 4")
    print ("1, 2, 3, or 4")

    what = int(input())
    if what == 1:
        print("here is the list", list)
        input("Press enter to continue")
        continue
    elif what == 2:
        itemadd = int(input("How many items would u like to add to the file "))
        for i in range(itemadd):
            item = input("What woud u like to add??        ")
            list.append(item)
            print("Added item(s) to the list")
            time.sleep(1)
            continue
    elif what == 3:
        print("What needs to be removed")
        print("Be precise")
        removal = input()
        list.remove(removal)
        print("Removed items from the list") 
        time.sleep(2)
        continue
    elif what == 4:
        print( "Thanks for using me." )
        with open(datafile,"w") as file:
            json.dump(list,file)
        print("Saved succesfully i Hope")
        print("Auto exiting now")
        time.sleep(2)
        clist = 2
        sys.exit

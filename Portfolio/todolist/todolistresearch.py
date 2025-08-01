################################################################################################################################################

# create the list
#my_list = []
# find  the number of elements you would like to enter
#num_elements = int(input("Enter the number of elements: "))
# for the amount of elements you want to enter
#for i in range(num_elements):
# ask for a point to list
#   element = input("Enter an element: ")
#   my_list.append(element)


################################################################################################################################################
# shows the list
#print("Your list:", my_list)

# now how to save in a file
#imports json library
import json
# shows an list with already existing things
#my_complex_list = [{"name": "Awice", "age": 30}, {"name : Bob", "age : 25"}]
# locates the file and stores it in var
#file_path = "test/todolist/data.json"

# finds the file and selects it
#with open(file_path, 'w') as file:
#
# removes all from the file imports the list to the file
#   json.dump(my_list, file)


################################################################################################################################################
#import json
#file_path = "test/todolist/data.json"

# it will  try to do a task
#try:
# tries to open the file and store the data in f
#    with open( file_path, 'r') as f:
        # stores the data in a python list
#        data_list = json.load(f)
    #shows the list
#    print(data_list)
    #shows the type of list
#    print(type(data_list))
# shows the error if the file isnt found
#except FileNotFoundError:
 
 #   print("Error: 'data.json' not found.")
# shows an error if there is no correct json format in the file
#except json.JSONDecodeError:
 
#    print("Error: Invalid JSON format in 'data.json'.")
################################################################################################################################################
#example of list
#my_list = ["apple", "banana", "cherry"]
# shows how to remove
#my_list.remove("banana")
# shows the new list
#print(my_list) # Output: ['apple', 'cherry']
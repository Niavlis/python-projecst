import random

import statistics

# dit is wat ik zelf heb bedacht
#print("How many repititios")
#amount = int(input())


#for i in range(amount):
#    print(random(1.6, 4))


###############################################

#Wat ik online vind met analyzatie 
#random vol nummer tussen 1 en 100 
#random_integer = random.randint(1, 100)
#print(random_integer)


#################################################
#tests voor dicegamble

list = []

print ("How many nums")
amount = int(input())
for i in range(amount):
    number = random.randint(1,10)
    list.append(number)
print (list)

modelist = statistics.mode(list)
print ("the mode is ",modelist )




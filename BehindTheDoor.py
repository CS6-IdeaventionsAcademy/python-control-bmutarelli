#Brogan Mutarelli
#Behind the door game show
#CS

door1 = "Iphone X"
door2 = "Egostia"
door3 = "Freshly Used Toilet (Unflushed)"
door4 = "$1000"

import random

door = random.randint (1,4)

print ("You are on the last question")
user_door = input ("Pick your door (1-4): ")



if user_door == "1":
    print ("You got a brand new " + door1)
    
elif user_door == "2":
    print ("You got a brand new " + door4)

elif user_door == "3":
    print ("You got a brand new " + door3)

elif user_door == "4":
    print ("You got a brand new " + door4)


else user_door not in ["1", "2", "3", "4"]:
    print ("That is invalid")
    user_door = input ("Pick your door (1-4): ")

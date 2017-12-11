# Brogan
# November 19 2017
# Python Beginnings
# 7 Favorite Color

yes = "yes"

color = "blue"

user_color = input ("What is your favorite color?  ")
# RCH: Your program should loop over and over if the user_color is not equal to your color
# This will only ask once. Please fix.  
while user_color == color:

    print ("Me too! What a coincidence!")
    yes = "no"
    break

if yes == "yes":

    print ("Thats not my favorite color. What is wrong with you. You should have the same favorite color as me!")

print ("""

See ya later!""")





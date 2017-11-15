#Brogan Mutarelli
#11/15/2017

import time

login =  "Brogan"
password = "drones"



login_user = input ("Username: ")

if login_user == login:

    password_user = input ("Password: ")
    if password_user == password:
        print ("Access Granted")
        time.sleep (1)
        print ("Go CapCOM")
        time.sleep (1)
        print ("Booting Up")
        time.sleep (1)
        print ("Accelaration Sensors Working")
        time.sleep (1)
        print ("Gyroscopic Sensors Working")
        time.sleep (1)
        print ("All Systems Go")
        time.sleep (0.5)
        print ("Rocket Launching")
        time.sleep (0.5)
        print ("Rocket Lacunch Affirmitive")
        break

    else:
            print("Access Denied")
    time.sleep (0.5)
    print ("System self destruct in:")
    time.sleep (0.5)
    print ("3")
    time.sleep (0.5)
    print ("2")
    time.sleep (0.5)
    print ("1")
    time.sleep (0.5)
    print ("Boom")
    time.sleep (0.5)
    print ("Bang")
    time.sleep (0.5)
    print ("You were blown into smithereens")

else:
    print("Access Denied")
    time.sleep (0.5)
    print ("System self destruct in:")
    time.sleep (0.5)
    print ("3")
    time.sleep (0.5)
    print ("2")
    time.sleep (0.5)
    print ("1")
    time.sleep (0.5)
    print ("Boom")
    time.sleep (0.5)
    print ("Bang")
    time.sleep (0.5)
    print ("You were blown into smithereens")


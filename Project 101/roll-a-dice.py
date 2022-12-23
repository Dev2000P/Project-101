import random
response=input("Would you like to roll the dice? y for yes, n for no: ")
while response=="y":
    number=random.randint(1,6)

    if number==1:
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    elif number==2:
        print("[   0 ]")
        print("[     ]")
        print("[ 0   ]")
    elif number==3:
        print("[   0 ]")
        print("[  0  ]")
        print("[ 0   ]")
    elif number==4:
        print("[ 0 0 ]")
        print("[     ]")
        print("[ 0 0 ]")
    elif number==5:
        print("[ 0 0 ]")
        print("[  0  ]")
        print("[ 0 0 ]")
    else:
        print("[ 0 0 ]")
        print("[ 0 0 ]")
        print("[ 0 0 ]")
    response = input("y to roll, n to exit: ")
quit()
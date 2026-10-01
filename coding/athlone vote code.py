athlone = input("are you living in athlone enter Y or N")
if athlone == ("y"):
    age = input("enter your age")
    age = float(age)
    if age >=18:
        registered = input("are you registered to vote enter Y or N")
        if registered == ("y"):
            print("you are able to vote")
        else:
            print("you must register to vote")
    else:
        print("you must be 18 to vote")
else:
    print("you must live in athlone")
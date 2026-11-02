option = input("enter a option of the weather,day or date ")
if option == ("weather"):
    weather = input("Is it sunny or rainy ")
    if weather == ("sunny"):
        print ("It's a happy day")
    elif weather ==("rainy"):
        print ("It's a sad day")
elif option == ("day"):
    day = input("enter a day of the week ")
    if day == ("saturday") or day == ("sunday"):
        print("Its a happy day")
    else:
        print("its a sad day")
# elif option == ("date"):
#     date = input("enter a date")
#     date = float(date)
#     if date 
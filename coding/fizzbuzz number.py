number = input("type an integer")
number = float(number)
if number %5 == 0 and number %3 == 0:
    print("fizzbuzz")
elif number %3 == 0:
    print("buzz")
elif number %5 == 0:
    print("fizz")
    


triangle = input("enter angle 1")
triangle = float(triangle)
triangle2 = input("enter angle 2")
triangle2 = float(triangle2)
triangle3 = input("enter angle 3")
if triangle == 0 or triangle2 == 0 or triangle3 == 0:
    print("this is not a valid triangle")
elif triangle + triangle2 + triangle3 == 180:
    print("this is a valid triangle")
else:
    print("this is not a valid triangle")
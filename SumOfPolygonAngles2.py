#Sum Of Polygon Angles.
print()
print("Sum of Polygon Angles:- ")
print()
def sum_of_polygon(side):
    if (side <= 2):
        print()
        print("This Is Not A Polygon.")
        print()
    else:
        print()
        angle = (side - 2) * 180
        print("Angle Of Polygon: ", angle)
        print()

def Enter():
    print()
    side = int (input ("Enter Sides Of The Polygon: "))
    print()
    sum_of_polygon(side)

Enter()



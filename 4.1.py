# Define a variable for pi
pi = 3.1415
# code to find area of a square
def square(side):
    area = side * side
    print("The area of the square is " + str(area) + " square units.")
# code to find area of a circle
def circle(radius):
    area = pi * radius * radius
    print("The area of the circle is " + str(area) + " square units.")

# Test the functions with chosen numbers
square(7)
circle(8)

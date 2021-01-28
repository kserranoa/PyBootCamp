#Ask the user for the radius of a circle and then print the area
def calculateArea():
    circle_radius = float(input("Enter the radius of the circle \n >>> "))
    pi = 3.14159
    circle_area = pi * (circle_radius**2)
    response = print("You entered", circle_radius, "the area of the circle is", circle_area)
    return response

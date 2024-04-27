#CS 4710
#JJ Holbrook
#700514202
#ICP 1 Question 5

import math


'''
The radius of a circle is 30 meters.
• Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
• Calculate the circumference of a circle and assign the value to a variable name of
_circum_of_circle_
• Take radius as user input and calculate the area
'''

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_circumference(self):
        return 2 * math.pi * self.radius
    
# Create a circle object with a radius of 30 meters
circle = Circle(30)

# Access the radius attribute of the circle object
print("Radius of the circle:", circle.radius, "meters")

# Create a circle object with a radius of 30 meters
circle = Circle(30)

# Calculate the area of the circle
_area_of_circle_ = circle.calculate_area()

# Print the area of the circle
print("Area of the circle:", round(_area_of_circle_, 4), "square meters")

# Take radius input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area using the formula
area = math.pi * radius ** 2

# Calculate the circumference using the formula
circumference = 2 * math.pi * radius

# Display the result with the calculated circumference
print("Circumference of the circle:", round(circumference, 4), "meters")

# Calculate the area using the formula
area = math.pi * radius ** 2


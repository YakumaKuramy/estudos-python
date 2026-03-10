import math

# Let's ask the user to enter the value of the radius and height of cone ray 

radius = input("Enter the value of the cone radius: ")
height = input("Infuse the cone height value: ")

"""
Please note that we do not have treatments in case the user informs
a floating point, in the next modules we will make this correction duly
"""
radius = int(radius)
height = int(height)

"""
Here we will calculate the total area of the cone and its volume!

Ab = πr2
As = πrg
At = Ab + A
V = (Ab * h) / 3
"""

generator = math.sqrt((radius ** 2) + (height ** 2))

base_area = math.pi * (radius ** 2)
side_area = math.pi * radius * generator
total_area = base_area + side_area
volume = (base_area * height) / 3

print(f"\nThe value of the cone height is {height}cm")
print(f"The radius value of the base of the cone is {radius}cm\n") # we put the '\n' to live a blank line
print(f"With this, the total area is {total_area}cm²")
print(f"The volume is {volume}cm³")

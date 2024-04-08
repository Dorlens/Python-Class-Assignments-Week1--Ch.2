#Dorlens Janvier Chapter 2 question 4


import math

radiusOfASphere = float(input("Enter the radius of a sphere"))

diameter = 2 * radiusOfASphere

circumference = 2 * math.pi * radiusOfASphere

surfaceArea = 4 * math.pi * radiusOfASphere**2

volume = 4/3 * math.pi * radiusOfASphere**3

print("The diameter is: ",diameter)
print("The circumference is: " ,circumference)
print("The Surface Area is: " ,surfaceArea)
print("The volume is: " ,volume)
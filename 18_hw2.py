# Write program to Find the area of the circle

import math
def calculateArea(radius):
    area = (math.pi * (radius**2))
    return area

n = int(input("Please enter the amount of circles you wish to test: "))

print("{:10} {:15} {:15}".format("Circle('s)","Radius Given","Calculated Area") )
print("{:10} {:15} {:15}".format("-"*10,"-"*15,"-"*15) )


for x in range(1, n + 1):
    print("{:10} {:15} {:15}".format(x, x, calculateArea(x)) )
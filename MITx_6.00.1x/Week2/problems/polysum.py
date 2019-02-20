import math

'''
polysum:

The function returns the sum of area and square of the perimeter for a given polygon.
The result is rounded off to 4 decimal places.
'''
def polysum(n, s):
    area = ((n*math.pow(s,2))/4)/math.tan(math.pi/n)
    perimeter = n*s
    
    return round(area + math.pow(perimeter,2),4)

sides = 4
length = 2.21

print("For a polygon of {0} sides with each side of {1} length, the result is: {2}".format(sides, length, polysum(sides,length)))

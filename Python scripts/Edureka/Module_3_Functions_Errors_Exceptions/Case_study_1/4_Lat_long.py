# Author : Gaurav
# Write a program to find distancebetween two locations when their latitude and longitudes are given.

from math import radians, sin, cos, acos

print("Input coordinates of two points:")
slat = radians(float(input(" Enter Starting latitude: ")))
slon = radians(float(input(" Enter Ending longitude: ")))
elat = radians(float(input("Enter Starting latitude: ")))
elon = radians(float(input("Enter Ending longitude: ")))

dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
print("The distance is %.2fkm." % dist)
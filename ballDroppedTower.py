import math

"""A ball is again dropped from a tower of height h with initial velocity zero. A
program that asks the user to enter the height in meters of the tower and then calculates
and prints the time the ball takes until it hits the ground, ignoring air resistance."""


#user inputs hieght of tower
h = float(input("Enter the height of the tower:"))
#time interval
t= float(input("Enter the time interval:"))

s = 9.81*t**2/2
print("The hight of the ball at is", h-s,"meters")

# s is set to calculates and prints the time the
#ball takes until it hits the ground,ignoring air resistance

t1= math.sqrt((h*2)/9.81)
print("Time it takes for ball to hit the floor ",round(t1,2),"secs")

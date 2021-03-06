

#function with conditional statement
def average_list_conditional (n):
    if len(n) == 0:
        print("The average of", n, "is", 0)
        return 0
    else:
        print("The average of", n, "is", sum(n)/len(n))
        return sum(n)/len(n)





# function to return the average of a list of numbers

def average_list (n):
    print("The average  of", n, "is", sum(n)/len(n))
    return sum(n)/len(n)

average_list ([1,2,3,4,5])
average_list ([1,2,3,4,5,6,7,8,9,10])
average_list ([1,2,3,4,5,6,16,17,18,19,20])



#while loop	

x = 0
while x<5:
    print(x)
    x = x + 1



#for loop

for x in range(5):
    print(x)

for x in range(26,30):
    print(x)

for x in range(20,31,5):
    print(x)



days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days:
    print(day)
print("\n")

# stop
for day in days:
    if day == "Wednesday":break
    print(day)
print("\n")

# skip
for day in days:
    if day == "Wednesday":continue
    print(day)
print("\n")

# import math module
import math     
print(math.pi)



#list 

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = (areas [3] + areas[-3])

# Print the variable eat_sleep_area
print(eat_sleep_area) 

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs

print (downstairs)
print (upstairs)

#! Slicing and dicing

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas [:6]
print(downstairs)
# Alternative slicing to create upstairs
upstairs = areas [6:]
print(upstairs)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas [-1]=10.50

# Change "living room" to "chill zone"
areas [4]="chill zone"

print(areas)

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,"bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1= areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)
# or 
areas_copy = areas[:]

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)


# !Function 


# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full , reverse = True)

# Print out full_sorted
print (full_sorted)

# !String Methods

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up

place_up = place.upper()

# Print out place and place_up

print(place)

print(place_up)


# !List Methods
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0

print(areas.index(20.0))

# Print out how often 9.50 appears in areas

print(areas.count(9.50))


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size

areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas )

# Definition of radius
r = 0.43


#!Import package

# Definition of radius
r = 0.43

# Import the math package
import math 
pi = math.pi
# Calculate C
C = 2*pi*r

# Calculate A
A = pi*r**2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Definition of radius
r = 192500

# Import radians function of math package
from math import radians


# Travel distance of Moon over 12 degrees. Store in dist.
dist = radians(12) * r

# Print out dist
print(dist)


# ! NumPy
# ? why we use NumPy
# consume less memory
# easy to manipulate
# faster the python list
# Support element wise operations
# elements are stored contiguous
# NumPy in github => https://github.com/numpy/numpy 
# pip3 install numpy => install numpy 


# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np 

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
print ( np_baseball)


# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball= np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))
print (np_baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
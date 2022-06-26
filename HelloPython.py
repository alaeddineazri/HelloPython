

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





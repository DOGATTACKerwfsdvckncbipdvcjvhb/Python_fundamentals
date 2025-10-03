#user input in python yayayayayayay

print("\n--------------INPUTS BY USER--------------")
print("commented out")
# name = input("Enter your name: ")
# print("your name is: ",name)

# age = int(input("Enter your age: "))
# print("your age is: ", age)

# print(type(age))
# age2 = input("Enter your dogs age: ")
# dogage_better= int(age2) 
# print(type(age2))
# print("next year, your dog will be: ",dogage_better+1)
# print(type(dogage_better))

# print("\n\n")
# height = float(input("enter height in meters: "))
# print("is your height: ",height ,"meters")
# print(type(height))


print("\n\n--------Challenges---------------")

#challenge 1

favcolor = input("What is your favorite color: ")
print("so is your favorite color, ",favcolor, "? because my dog hates it")

#Challenge 2
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

print("your sum of those two numbers is: ", x+y)

#challenge 3
import math
diameter = float(input("Input a diameter of a circle: "))
area = math.pi*pow(diameter/2, 2)
print("your area of the circle is: ", area)

#custom die roll # challenge 4

import random
sides = int(input("how many sides should your die have: "))
sides = math.floor(sides)
if sides < 1:
    print("no negative numbers or zeros")
    
else:
    chooserandomside = random.randint(1, sides)

    print("you rolled and got the side: ",chooserandomside)
    

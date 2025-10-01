#Python libraries, libraries are things that add functions to make coding easier, it is very useful.
import math

print("Square root: ", math.sqrt(25))
print("Round up to integer: ", math.ceil(4.2)) #round up is ceil as in ceiling because the ceiling is up.
print("Round down to integer: ", math.floor(4.8)) #round down is floor as in flooring because the flooring is down.
print("Power: ", math.pow(2,5)) #pow is power for exponents like 2^5 because pow is the first 3 letters of power
print("Pi: ", math.pi) #pi is for pi because pi is 3.141592...


#-------------------------------------------
# Random library
#-------------------------------------------




#challenge part 1
seed = 589.32

randomNum = seed/ 250

randomNum = randomNum + 40

randomNum = randomNum *2

print("\n\nPseudo random number: ", math.floor(randomNum))

#challenge bonus

seed2 = 500.12

randomNum2 = seed2/240

randomNum2 = randomNum2 + 2

randomNum2 = randomNum2 *1.1
print("\n\nPseudo random number bonus: ", math.floor(randomNum2))

# RANDOM LIBRARY PART 2
import random
print("------------RANDOM LIBRARY-------------")

i = 0
y = 0
while i < 10000:
    x = random.randint(1, 100)
    print(x)
    
    
    i = i+1


#LISTSSSSSSSS (this is really just an array tbh)
mylist = ["eeg", "CHICKEN JOCKEY", "67", "76", "THE NETHER"]
x2 = random.randint(0,4)

print("\n\n")
print("---------------------LIST RANDOM STUFF------------------------")
print(random.choice(mylist))
print("print the whole list: ",mylist)
random.shuffle(mylist)
print("print the shuffled list: ",mylist)

#CHALLENGE 1
radius = 14/2
circle_area = math.pi*pow(radius, 2)

print("\n\n--------------------Challenges-------------------------")
print("circle area of diameter of 14: ", circle_area)

#challenge 2
die_roll = random.randint(1,6)
print("\nRandom dice roll: ", die_roll)

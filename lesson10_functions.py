#python functions are simply blocks of code that can be reused.
# to run a function, you *call* a function by writing its name, followed by parenthesis, and any arguments that it needs.

print("example 1\n\n")
def addtwonumbers(a, b):
    sum = a+b
    return sum

# a = int(input("enter a number: "))

# b = int(input("enter another number: "))

az = addtwonumbers(5,4)

print(az)

print("\n\n\n\n\n\n\n\n\n")
print("Example 2\n\n")

def EXPRESSTHIS(a,b,s): ##e is called a parameter, which is a placeholder for an argument
    answer = 0
    if s == '+':
        answer = a+b
        return answer
    elif s == '-':
        answer = a-b
        return answer
    elif s == '*':
        answer = a*b
        return answer
    elif s == '/':
        answer = a/b
        return answer

# a = int(input("Enter a number this comes first: "))
# b = int(input("Enter a number: "))
# symbol = input("enter a symbol(*,+,-,/): ")

expression = EXPRESSTHIS(2,2,"/") ## the thing inside here is the expression.
print(f"Your answer is {expression}")

print("\n\n\n\n\n\n\n\n\n\nexample 3\n\n\n\n\n\n")

def greeter(name):
    return f"hi {name}!"
first = greeter("CHADGSFCBV")
second = greeter("teodfa")
third = greeter("Wet head")
print(first, second, third)

print("\n\n\n\n\n\nexample 4\n\n\n\n")

def remainder(a,b):
    
    
    sum = a%b
    return f"The remainder of {a} divided by {b} is {sum}"

# print(remainder(int(input("enter a number(first): ")), int(input("enter a number: "))))
print(remainder(5,5))

print("\n\n\n\n\nexample 5\n\n\n\n\n\n")

def is_far(distance):

    if distance < 1:
        return"enter something greater than zero"


    if distance >= 300:
        return "thats far"
    elif distance < 100 and distance > 20:
        return "thats not too far"
    else:
        return "thats nearby"
    
print(is_far(-10))

print("\n\n\n\n\n\n\n\n\n\n")

#I want to create a function that takes in a number and doubles it, then adds it to a list.
# the function should also take in a number of times that we should double the number

def doubler(a,amount):
    sum = a
    list = []
    for i in range(amount):
        sum = sum*2
        list.append(sum)
        
    
    return f"The list for the numbers are {list}, the ending number is {sum}"

print(doubler(int(input("Enter a number: ")), int(input("Enter amount of times you want it doubled: "))))
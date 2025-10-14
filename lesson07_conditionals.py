#conditionals in py
#comparison operators: ==, !=, <, >, <=, >=
#logical operators: and, or, not
#control flow = if, elif, else
#loops: while, for
#Bools use this
#bools return true and false

# print("\n--- Conditionals in Python ---")
# print(3==2)
# print("Hello" == "Hi there")
# print( 7 != 4 )
# print(4 > 5)

#if
num = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
if num == num2:
    print(f"{num} is equal to {num2}")
else:
    print(f"{num} is not equal to {num2}")

print()
if num <= num2:
    print(f"{num} is less than {num2}")
else:
    print(f"{num} is greater than {num2}")
print()
#elif, is just else if
temp = float(input("Enter a temperature f: "))
if temp >= 80:
    print("it is hot")
elif 80 > temp and temp >= 60:
    print("it is nice outside")
else:
    print("it is cold\n\n")

x=2
y=20
if x==y:
    print("x is equal to y\n\n")
elif x >y:
    print("x is greater than y\n\n")
elif x <y:
    print("x is less than y\n\n")
else:
    print("error\n\n")

age = 17
has_per = True

if age >= 17 and has_per:
    print("You can drive")
else:
    print(f"you can't drive yet wait until you have permission or you need to wait {17-age} year/years")

print("using or\n\n\n")
day = input("Enter a day: ")
day = day.capitalize()
print(day)
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("it is a weekday")

if day != "Monday":
    print("\nit is not monday")
else:
    print("\nI hate school")

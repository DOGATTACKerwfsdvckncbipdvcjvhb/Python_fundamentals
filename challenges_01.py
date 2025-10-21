#Palidrome challenge
x = input("Input palidrome: ")
x=x.lower()

if x==x[::-1]:
    print(f"{x.capitalize()} is a palidrome")
else:
    print(f"{x.capitalize()} is not a palidrome")

#Domain from email
emailinput = input("Enter your email: ")
emailindex = emailinput.index("@")
emaildomain = emailinput[emailindex+1::1]
print("Your domain is: ",emaildomain)

#List finding last thing in list
list1 = ["CHICKEN", "BANANA", "ORANGE"]
input2 = input("Input a thing from the list given above: ")
if input2.upper() == list1[2]:
    print("YOU ARE RIGHT YAYAYA")
else:
    print("You are wrong")

#challenge 4
word = input("Input a word: ")
word = word.lower()
if len(word) >= 3 and "ly" not in word:
    
    if "ing" in word:
        print(word+"ly")
    elif "ing" not in word:
        print(word + "ing")
    else:
        print("ERROR")
else:
    print("NO WORDS BELOW 3 LETTERS and no ly at end")
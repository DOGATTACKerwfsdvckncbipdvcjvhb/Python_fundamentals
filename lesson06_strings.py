#basic string creation and indexes:

greeting = "hello"
name = "person"

print(greeting +" "+ name)

# 0 1 2 3 4
# H e l l o

# 0 1 2 3 4 5 
# p e r s o n

#concatenation
message = greeting + " " + name + "!!!"
print("Concatenated message: ", message)

secondLetter = greeting[1]
print(secondLetter, "is the second letter of hello\n")

word = "Super-cali-fragil-istic-expi-ali-docious"

print("first letter of Super-cali-fragil-istic-expi-ali-docious: ", word[0])
print("Last letter of Super-cali-fragil-istic-expi-ali-docious: ", word[-1])
print("range of letters (non-inclusive): ", word[3:7])
print("another range of letters (non-inclusive): ", word[-7:-2])
print("first five letters of Super-cali-fragil-istic-expi-ali-docious: ", word[0:5])
print(word[:5])
print("last seven letters: ", word[-7:])
print()
print("step through every second letter of that big word: ", word[::2])
print("print that word reversed: ", word[::-3])

## Built in fuction
country = "India"
length_of_word = len(country)
print("length of the country name 'India' ", length_of_word)

phrase = "ChIckEN JoCkEY sIX sEVeN AT SiX SeVEn"

print("\norignal phrase: ", phrase)
print("fixed phrase for uppercase: ", phrase.upper())
print("fixed phrase for lower case: ", phrase.lower())
print("Capitalized word that is proper for sentances: ",phrase.capitalize())
print("Title format: ", phrase.title())

##chicken jockey 67 at 676767 cuz 67 the nether
#Find and replace text
sentence = "My dog is a very goofy goober."
print(sentence)
Newsentence = sentence.replace("My dog","A goofy goober")
print(Newsentence)
nextsent = sentence.replace("goofy", ",VERY, goofy")
print(nextsent)

#Formated strings
print("\n--------Formated strings-------------")

name = "'My name'"
age= 6.7 
city = "Ohio city"

print(f"Hello, my name is {name}. I am {age} years old and I live in {city}.")
name = "the nether"
print(f"Next ohio year, I will be {int(age*10)} and my new na me will be {name.upper()}.")

#challenge 1: Favorite quote

x = input("input a quote: ")
print("the length of your quote is: ", len(x))

#challenge 2: name formatter
name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name + ", " + name)
print(f"{last_name}, {name}")

#challenge 3: word mutations
phrase = input("Enter a phrase: ")
print("\nreversed phrase: ", phrase[::-1])
print("Uppercase phrase: ", phrase.upper())
print("Lowercase phrase: ", phrase.lower())
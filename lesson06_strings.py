#basic string creation and indexes:

greeting = "hello"
name = "person"

print(greeting +" "+ name)

# 0 1 2 3 4
# H e l l o

# 0 1 2 3 4 5 
# p e r s o n

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
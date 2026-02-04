## Function challenges

##sudo for challenge 1

##defined addition(num,anum)
##{
##  sum <- num+anum
##  return sum
##}

##defined subtraction(num,anum)
##{
##  sum <- num-anum
##  return sum
##}


##defined multiply(num,anum)
##{
##  sum <- num*anum
##  return sum
##}

##defined divide(num,anum)
##{
##  sum <- num/anum
##  return sum
##}

##challenge 1 code
print("--------------challenge 1----------------")

def add(num,anum):
  sum = num+anum
  return sum

def subtraction(num,anum):
  sum = num-anum
  return sum


def multiply(num,anum):
  sum = num*anum
  return sum

def divide(num,anum):
  sum = num/anum
  return sum


print(add(3,3))
print(subtraction(14,5))
print(multiply(13,33))
print(divide(41,4))
print("\n\n\n\n-------------------challenge 2------------------")

##sudo for challenge 2

#define aver(x,y,z)
#{
#   mean <- x+y+z
#   mean <- mean/3
#   return mean
#}

#print(aver(5,4,3))


#code is for challenge 2

def aver(x,y,z):
   mean = x+y+z
   mean = mean/3
   return mean

print("the average of 5,4,3 is: ", aver(5,4,3))


print("\n\n\n\n-------------------challenge 3------------------\n\n\n\n")

##sudo for challenge 3

##define is_even(num)
#{
#   if((num%2) == 0) {
        #return "even"
    #} else {
        #return "odd" 
    #}
#
#}

# code for challenge 3

def is_even(num):
  if (num%2) == 0:
    return "even"
  else:
    return "odd"
  
num = 24
print(f"The number {num} is: {is_even(num)}")
print("\n\n\n\n-------------------challenge 4------------------\n\n\n\n")

#sudo for challenge 4

#define analyze_word(word) 
#{  
#   if type(word) == "str":
#       return "error"
#   vowelCount <- 0
#   consonantCount <- 0
#   REPEAT for i in word{
#       if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' {
#           vowelCount+=1
#       } else {
#           consonantCount+=1
#       }
#   }
#   return f"The vowel amount is {Vowelcount} and the consonant amount is {consonantCount}"
#}

#print(analyze_word)

#code for challenge 4

def analyze_word(word):
    print(type(word))
    if isinstance(word, str): #isistance allows for you to check if a variable is a string
       return "error"
    vowelCount = 0
    consonantCount = 0
    for i in word:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowelCount+=1
        else:
            consonantCount+=1
    return f"The vowel amount is {vowelCount}, the consonant count is {consonantCount}."

print(analyze_word("string"))
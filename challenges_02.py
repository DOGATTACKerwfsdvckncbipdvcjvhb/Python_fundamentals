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
  

print("The number 5 is: ", is_even(5))
print("\n\n\n\n-------------------challenge 4------------------\n\n\n\n")
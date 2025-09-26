#KEY CONCEPTS: math operators: +, -, *, /, //, %, **
#  ** means power, // means divide but only with integers as the regular one gives floats
#  % means mod and it divides two numbers and gets the remainder
# 


add = 7+2
print("Sum: ", add)

subtr = 7-2
print("Difference: ", subtr)

multiply = 7*2
print("Product: ", multiply)

float_divide = 8/2
print("Float quotient: ", float_divide)

integer_divide = 7//2
print("Integer_divide: ", integer_divide)

modulus = 7%2
print("Modulus: ", modulus)

exponent = 7**2
print("Exponent: ", exponent)

print("is 2+2 = 10-6 = 2^2? ",2+2 == 10-6 == 2**2)
print("is 2+2 = 10-7 = 2^2? ",2+2 == 10-7 == 2**2)
result1 = (2+3)*4
print("\n\nResult 1(for pemdas): ", result1)

result2 = 2**3*4
print("Result 2: ", result2)

result2b = 4*2**3
print("Result 2b: ", result2b)

result3 = 20/5*2
print("Result 3: ", result3)

result4 = 10-2+3
print("Result 4: ", result4)

result5 = 5+2**3 *(4-1)
print("Result 5: ", result5)

#Challenges

#Challenge 1: rectangle Area

area = 8*5
print("\n\n\nArea: ", area)

#Challenge 2: Circle Area

areacircle = 3.14*7**2
print("Circle Area: ", areacircle)

#Challenge 3: Shopping Total

costofpurchase = (12.99*3) + (3.50*4)
print("Cost of purchase for total: $",costofpurchase)

#Challenge 4: Even or odd

evenorodd = 124892%2

if evenorodd == 0:
    print("EVEN, if the remainder is 0 and the number is divided by 2 it is EVEN")
else:
    print("ODD if the number is divided by 2 and the remainder is 1 then it is ODD")


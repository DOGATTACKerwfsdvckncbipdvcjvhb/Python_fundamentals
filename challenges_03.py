import math
import sys
import string

# def ints_only(a, b):
#     if isinstance(a,int) and isinstance(b,int):
#         return True
#     else:
#         return False

# boolean = ints_only('2',1)
# print(boolean)

def functions(listofnumbers):
    count=1
    for i in listofnumbers:
        if count == len(listofnumbers):
            break;
        if i != listofnumbers[count]: 
            
            return False
        count+=1
    return True
print(functions([1,1,1,1]))



# def palidromefinder():
#     word = input("Enter a word: ")
    
#     if word[::-1] == word:
#         return True
#     else:
#         return False
    
# print(palidromefinder())


num = 4
while num <= 2:
    num+=2
print(num)
while num <= 7:
    num+=1
print(num)
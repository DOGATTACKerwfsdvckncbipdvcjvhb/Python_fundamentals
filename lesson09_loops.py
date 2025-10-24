#loops in python
#two loops: for and while, in c/c++ for is better usually

print("\n---Loops in python---")

#for loop

thoongs = ["gawfs","sixseven","nether","wowwsers","threehundred"]
##thing was intentinally spelt wrong 
print("\nThing list: ", thoongs)
print("\nFor loop: visiting each thing")

import time
c = 0
for thing in thoongs:
    print("Looking at the thing: ",thing)
    time.sleep(1.5)
    x = input("what do you think will be looked at next: ")
    x.lower()
    c = c+1
    if x == thoongs[c]:
        print("Yay you got it, now we leave")
        break
    else:
        print("you got it wrong")
        print("going to next thing")
        print("thing number you on: ",c)
        
    


for i in range(5):
    print("counting:  ",i)
#three arguments start, stop and step
   
print("\n\n\n")
for i in range(2,11,2):
    print("counting:  ",i)


#break can allow it to go out of function early I learned this in C/C++
#continue goes to the start of a loop





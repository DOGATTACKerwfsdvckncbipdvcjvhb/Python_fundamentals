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
    time.sleep(0.1)
    # x = input("what do you think will be looked at next: ")
    # x.lower()
    # c = c+1
    # if x == thoongs[c]:
    #     print("Yay you got it, now we leave")
    #     break
    # else:
    #     print("you got it wrong")
    #     print("going to next thing")
    #     print("thing number you on: ",c)
        
    


for i in range(5):
    print("counting:  ",i)
#three arguments start, stop and step
   
print("\n\n\n")
for i in range(2,11,2):
    print("counting:  ",i)


#break can allow it to go out of function early I learned this in C/C++
#continue goes to the start of a loop

print("\n\n\n---Iterating over strings---")



favWORD = "LINGANGUUUU"

letter_list = []

for letter in favWORD:
    print(letter,end=" ")
    letter_list.append(letter)
    print(letter_list)

print()
print(letter_list,"\n")

#WHILE LOOPS
#while works with conditionals and for does not in python, so sad fors are so much better in C
#SIXSEVEN

print("---While loops---")

count = 0
while count < 5:
    print(f"looping, we are on loop number {count}")
    count += 1
    time.sleep(0.1)

print("done with loop")
userinput = ''
while userinput != 'exit':
    userinput = input("type 'exit' to escape: ").lower()
    if userinput == 'exit':
        print("Exited")

countbutcool = 60
increment = 1

while countbutcool > 0:
    
    if countbutcool-increment< 0:
        print("Emergency exit")
        break
    countbutcool-= increment
    increment+=1

    print("countdown: ", countbutcool)
    
    time.sleep(0.05)

#CHALLENGES


#CHALLENGE 1

listofruit = ["Straw Berry", "Banana", "Orange","Raisin","Tomato","Cranberry","Jackfruit"]
x = int(input("Enter how many fruits you want to pick: "))

import random
for i in range(x):
    print("Getting this fruit: ", random.choice(listofruit))
#YAY IT DONE LETS GO LIN GAN GULI GULI GULIII GWATCHA LIN GAN GUUUUUU LIN GAN GUU
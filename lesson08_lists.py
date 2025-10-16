#lists in python
#lists store multiple values in one variable.
#they are ordered, mutable (Changeable), and allow duplicates.

print("\n---Lists in python---")

Things = ["GHNJMY GHBFCVX", "gfhbgergtrfb", "thergf", "egrfb"]
nums = [1,2,5,1,2,4,7,7,5,6,2,1,0,10,20,30,4.5,1.333,-102]
mixed = ["gdbf", 2, True, "23r4e"]


print("\n\n\n---Indexing how to access the elements of a list---")
print("first element of Things list: ", Things[0])
print("second element of Things list: ", Things[1])
print("last element of Things list: ", Things[len(Things)-1]) #this
# or this
print("last element of Things list using diff method: ", Things[-1])

print("\n---Modifiying Lists---")
print("Original list: ", Things)
Things[0] = "io8hyu9nm"
print("Modified list: ", Things)
Things.append("3535535")
print("Modified 2list: ",Things)

#insert element at specific index
print("\n\n---Inserting things into lists in the middle of the list---")
Things.insert(3,"rejhvk lcdj")
print("Instered one thing, new list: ", Things)
Things.insert(5,"wegiurbfjqa2w1edrf")
print("Instered one new thing, new list: ", Things)
Things.remove(Things[1])
print("Removed second thing: ", Things)

thelastthing = Things.pop()
print("removed: ", thelastthing)
print("the new list: ",Things)

ThingToReplace = Things.index(Things[3])
print(ThingToReplace)
print(Things)
Things[ThingToReplace] = "e42fvyb7 6t7yg6767"
print(Things)

print("\n\n----Useful list functions----")
print("Original numbers list: ", nums)
print("Length of the list: ",len(nums))
print("Min: ", min(nums))
print("Max: ", max(nums))
print("Sum: ", sum(nums))
x3tegr = nums
x3tegr.sort()
print(x3tegr)
x3tegr = Things
print("Original List for things: ",x3tegr)
x3tegr.sort()
print("Sorted list: ",x3tegr)

nums.reverse()
print(nums)
#lists are like mutants because they can mutate I guess
#tables(arrays) can't mutate
print("\n\n ---Checking Membership---")

if "rejhvk lcdj" in Things:
    print("This thing is in the list: rejhvk lcdj\n")
else:
    print("This thing is not in the list: rejhvk lcdj\n")

print("---copying lists---")
new_list = [1,67,67]
copiedList = new_list.copy()
print("New list that is original: ", new_list)
print("Copied list of the previous one: ", copiedList)
copiedList.append(4)
print("Added new thing to copied list: ", copiedList,)
print("Preserves orignial list")

print("\n---Matrices/Nested lists---")
matrix = [
    [1,2,3],
    [4,5], 
    [6,7,8,9],
    [67,76]
    ]
print("A matrix: ", matrix)
print("2nd number of the last list in the matrix is: ", matrix[3][1] )
print("1st number of the last list in the matrix is: ", matrix[3][0] )
print("Sum of first number of second list and last number of first list: ", matrix[1][0] + matrix[0][-1])

print("\n\n---Challenges---")
#Challenge 1
numbers = [1,2,3,4,5,6]
print(numbers)
x=int(input("Enter a new integer for this list: "))
numbersNew = numbers.index(3)
numbers[numbersNew] = x
print(numbers)

#challenge 2

shopping=[]
shopping.append("orange")
shopping.append("banana")
shopping.append("jackfruit")
print("Shopping list: ", shopping)
shopping.remove("jackfruit")
print("New shopping list: ", shopping)
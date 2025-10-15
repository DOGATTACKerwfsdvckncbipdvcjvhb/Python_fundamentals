#lists in python
#lists store multiple values in one variable.
#they are ordered, mutable (Changeable), and allow duplicates.

print("\n---Lists in python---")

Things = ["GHNJMY GHBFCVX", "gfhbgergtrfb", "thergf", "egrfb"]
nums = [1,1,2,3,4,5,6]
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

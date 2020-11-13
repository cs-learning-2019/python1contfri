# Foucs Learning: Python Level 1 Cont
# More Loops with list
# Nov 13, 2020
# Kavan Lam

# Ex 1
for counter in range(0, 6):
    print(counter)
    

# Ex 2
print("--------------------------------")
counter = 0
while counter < 6:
    print(counter)
    counter = counter + 1
    
    
# Ex 3
print("----------------------------------")
myList = [15, 12, 3, 7]
for item in myList:
    print(item)
    

# Ex 4
print("----------------------------------")
myList = [15, 12, 3, 7]
index = 0
while index < len(myList):
    print(myList[index])
    index += 1  # This is shorthand notation for doing index = index + 1


# Ex 5
print("----------------------------------")
myList = [15, 12, 3, 7]
for counter in range(len(myList)):
    print(myList[counter])
    

# Ex 6
print("----------------------------------")
myList = [15, 12, 3, 7]
counter = 0
while counter < len(myList):
    print(myList[counter])
    counter += 1

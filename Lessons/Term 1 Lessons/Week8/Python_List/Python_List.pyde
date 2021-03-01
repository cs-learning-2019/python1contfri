# Focus Learning: Python Level 1 Cont
# Python List
# Kavan Lam
# Nov 6, 2020

# Cool we can have one variable for each student
age1 = 10
age2 = 7
age3 = 9
age4 = 8

# The above code is great but what if we had 1000 students. We would need 1000 variables
# and that is NOT good

# We can actually use a Python List to make this much better. In fact all we need is one variable
ages = [10, 7, 9, 8]  # <--- This is a Python List
# The way you want to think about a Python List is that it is basically a box which you
# can add stuff to. We use sqaure brakets to create a List

print(ages)  # You can print the whole list

# Ok now lets see what the worksheet has to say about Python List
print("-----------------------------------------------")
pets = [3, 5, 1, 9, 0, 2]  # The first number is in index or spot 0
print(pets[0])  # Print the number in spot/index 0
print(pets[3])
print(pets)

pets[2] = 6
pets[5] = pets[5] + 3
print(pets)

print(len(pets))  # len gives the length of something
print(len("Hello"))  # len can also give us how many characters in a string

# print(pets[8])  we can not do this since there is no index or spot number 8
print(pets[-1]) # index -1 is actually the last number in the list

# Lets do a new example
print("------------------------------")
students = [10, 20, 5, 35, 25, 15]
students.append(21)
print(students)

students.pop(2)  # use pop to remove a number from the list. Pop expects you to give it a index. So in our exmaple 2 is the index.
print(students)

# We can remove the last thing just by using pop without giving it an index
students.pop()
print(students)

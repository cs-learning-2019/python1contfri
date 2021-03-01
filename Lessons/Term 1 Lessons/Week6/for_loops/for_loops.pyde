# Focus Learning: Python Level 1 Cont
# For loops
# Kavan Lam
# Oct 23, 2020

# Ex1
# for (a variable) in (something):
for i in range(10):  # the general rule is range will go 1 less than what you say
    print(i)
    
# Ex2
print("----------------------------")
for num in range(15, 21):
    print(num)
    
# Ex3
print("----------------------------")
for p in range(4, 10, 2):
    print(p)
    
# Ex4
print("----------------------------")
for countdown in range(10, -1, -1):
    print(countdown)
    
print("Blastoff!!!")

# Ex3
print("----------------------------")
name = "Kavan"
for character in name:
    print(character)

# Ex4
print("----------------------------")
box_size = 8
print("-" * box_size)  # This is the first row

# All the middle rows
for row in range(box_size - 2):
    print("|" + " " * (box_size - 2) + "|")

print("-" * box_size)  # This is the last row

# Ex5
# Lets see an example of a double for loop
for num1 in range(3):
    for num2 in range(3):
        print(num1, num2)

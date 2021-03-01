# Focus Learning: Python Level 1 cont
# If statements Homework Solutions
# Kavan Lam
# Oct 9, 2020

# Question 1
"""
1) Deciding if a user clicked on a button
2) AI making decisions
3) A program that detects whether you are old enough to enter somewhere
"""

# Question 2
"""
Else is used to capture all other cases not described in the code. Elif is used to add more cases
to your if-statement usually making it more complicated. 
"""

# Question 3
x = 40
y = 70
if x+y > 100:
    print("Bye")
elif x+y > 20:
    print("Hello")
else:
    print("Cool")
    

# Question 4
"""
The problem with the given code is that it print you are a teen even though the age is 70.
To fix this you need to switch the order of the cases in the if-statement. Below is the correct
version and works as expected.
"""
age = 70
if age >= 65:
    print(“You are old”)
elif age >= 13:
    print(“You are a teen”)
else:
    print(“You are a child”)
    

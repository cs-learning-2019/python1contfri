# Focus Learing Python Level 1 Cont
# Intro to Python Homework
# Kavan Lam
# Sept 13, 2020

# Question 1
"""
A variable is like a helping hand that can hold on to data for you. We need to use
variables becasue a lot of the cool stuff we do in programming requires us to
have memory and hold on to data for later.
"""

# Question 2
"""
It is not possible to add a string with a float. Dividing a string with an integer is
also not possible. You can try the following and see what happens.

print("hh" + 7.89)
print("hh" / 2)
"""

# Question 3
# Bad Solution
print("*")
print("*" * 2)
print("*" * 3)
print("*" * 4)
print("*" * 5)

# Good Solution
print("----------------------------------------------")
for i in range(5):
    print("*" * (i + 1))

# Intro to Python
# Kavan Lam
# Sept 12, 2020

# Print is an exmaple of a function
print("Hello World") # String is anything in quotation marks ex "Ka+45678van"


print("h\te\n" * 3) # String multiplication  note that \n moves you to the next line and \t is a tab
# Also note that print adds an extra \n 


print("Hello " + "World " + "Bob") # String concatenation

score = 1 # score is a variable that is holding on to the int 1
print("My Score is = " + str(score))  # you can not add a string with an int

# In Python we have a lot of data and there are different types of data
"""
1) String 
2) Int
3) Float   Ex 5.5, 3.14, 56.9082
4) Boolean   Ex True, False
"""

# Extra Ex 1
print("-------------------------------------------------")
x = 5.17
print(int(round(x)))   # int() is a function that takes something and converts it into an int   also we can use the round funtion to round numbers

# Extra Ex 2
print("-------------------------------------------------")
print(int("56") + 1)
# print(int("56.78"))  not going to work since this is a string and we are trying to convert a dot into a number
print(int(56.78)) # int() will remove the decimal


# Extra Ex 2
print("-------------------------------------------------")
print(len("Hello")) # the len function gives the length of an object
x = 5678912   # x will be an int
print(len(str(x)))

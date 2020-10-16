# Focus Learning: Python Level 1 Cont
# If statements
# Kavan Lam
# Oct 16, 2020

# EX 1) Start off with a simple one
age = 20

# 8 > 1   > --> GREATER THAN
# 1 < 8   < --> LESS THAN
# : --> THEN
# Below is a single if statement
if age >= 18:   
    print("You are an adult.")
    
print("Yo")  # This line is outside the if statement

print("----------------------------------------------------")

# EX 2)
age = 11
if age >= 18:   
    print("You are an adult.")
else:  # This part extends the if statment. You are only allowed to use else once per if statment
    print("You are a child.")

print("----------------------------------------------------")

# EX 3)  This is bad code, the ordering of the cases is not correct
age = 90
# BTW the whole thing is one if statement
if age >= 18:   
    print("You are an adult.")
elif age >= 65:  # This is extending the if statmeent. You are allowed to use as many elif as you like.
    print("You are an old person.")
else:  # This part extends the if statment. You are only allowed to use else once per if statment
    print("You are a child.")
    
print("----------------------------------------------------")

# EX 4)  
age = 90
if age <= 17:
    print("You are a child.")
elif age <= 64:
    print("You are an adult.")
else:
    print("You are an old person.")
    
print("----------------------------------------------------")

# EX 5)
age = 11
if age <= 17:  # This is the first if-statments
    print("You are a child!!!!!!!")
    
if age <= 64: # This is the second if-statments
    print("You are an adult!!!!!!")
else:
    print("You are an old person!!!!!!!")
    
print("----------------------------------------------------")

# EX 6)
age = 100
cash = 1000001

if age == 11:   # ==  --> Is used for to test if the thing on the left is the same as the thing on the right
    print("I don't care.")
elif age == 100 and cash > 1000000:
    print("Old and rich!!!!")
elif age > 10 and cash >= 2000:
    print("Cool!!!")
elif age < 35 and cash < 6000:
    print("Super!!!!!")
else:
    print("Confused?????")
    
print("----------------------------------------------------")

# EX 7)
fav_color = "Blue"
is_cool = True

if not is_cool == True:
    print("You are the best!!!")
elif is_cool == False or fav_color == "Blue":
    print("BOOOO!!!!")

    
print("----------------------------------------------------")

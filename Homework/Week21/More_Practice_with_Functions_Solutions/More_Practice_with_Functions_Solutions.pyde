# Focus Learning: Python Level 1 Cont
# More Practice with Functions
# March 8, 2021
# Kavan Lam

# Question 1
# 1) 1z is not a valid variable name
# 2) You call the function but do not give it y and z
# 3) when you do x+y, y does not have a value
# 4) There is no :
    
def my_function(x, y, z):
    print("Hello there, good thing you are doing the HW")
    return x+y

print(my_function(1, 4, 5))

# Question 2
print("-------------------------------------")
def is_all_negative(num_list):
    is_all_neg = True
    
    for num in num_list:
        if num >= 0:
            is_all_neg = False
                
    return is_all_neg

print(is_all_negative([-2, -6, 0, 10, -8]))


# Question 3
print("-------------------------------------")
def question3(num_str, num):
    for string in num_str:
        if len(string) == num:
            return True
    
    return False

print(question3(["YO", "Bob", "YOU", "Cool"], 4))
    
        
        
        
        

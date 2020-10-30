# Focus Learning: Python Level 1 Cont
# While Loops
# Kavan Lam
# Oct 30, 2020

# Ex 1
# while (some condition)  <--- General form
counter = 8
while counter > 0:
    print(counter)
    counter = counter - 2
    
print("Hello")   # This line is not part of the while loop

# Ex 2
print("----------------------------------------------")
passby = False
total = 0
while passby == False:
    total = total + 2
    if total > 12:
        print("!!!")
    if total > 20:
        passby = True
        
# Ex 3
print("----------------------------------------------")
counter = 10
while counter > 0:
    print("This is amazing!")
    # counter = counter + 1 this is no good as it will make your code go on forever and ever
    counter = counter - 1

# When you do while loops you need to be carful with the condition. Sometimes you can
# end up with what we call an infinite loop

# Ex 4
print("----------------------------------------------")
x = 5
y = 0
while x > 0 or y < 3:
    x = x - 1
    y = y + 1
    print("Hello " + str(x) + " " + str(y))
    
# Ex 5
print("----------------------------------------------")
x = 5
y = 0
while x > 0 or y < 3:
    x = x - 1
    y = y + 1
    print("Hello " + str(x) + " " + str(y))
    if x == 3 and y == 2:
        break  # You can use this to break the while loop and stop looping


# Ex 6
print("----------------------------------------------")
x = 5
y = 0
while x > 0 or y < 3:
    x = x - 1
    y = y + 1
    if x == 1 and y == 4:
        continue # This will skip one loop but not break the while loop
    print("Hello " + str(x) + " " + str(y))


# Ex 7
print("----------------------------------------------")
name = "Bobby"
#for character in name:
#   print(character)

index = 0
while index < len(name):
    print(name[index])
    index = index + 1

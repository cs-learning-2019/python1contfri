# Focus Learning: Python Level 1
# Functions Homework Solutions
# Kavan Lam
# March 22, 2021

# Question 1
"""
def setup():
    size(900, 900)
    
def draw():
    background(0, 0, 0)
    draw_the_circles(10)
    
def draw_the_circles(num_of_circles):
    for c in range(num_of_circles):
        r = int(random(0, 255))
        g = int(random(0, 255))
        b = int(random(0, 255))
        fill(r, g, b)
        
        x = int(random(0, 900))
        y = int(random(0, 900))
        ellipse(x, y, 10, 10)
"""

# Question 2  --> 0, 1, 1, 2, 3, 5, 8, 13 .....
def fib(n):
    fib_nums = []
    next = -999
    current = 1
    previous = 0
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_nums = [0, 1]
    for i in range(n - 2):
        next = current + previous
        fib_nums.append(next)
        previous = current
        current = next
    
    return fib_nums

print(fib(10))
        
    
        
        
        
        
        
    
    

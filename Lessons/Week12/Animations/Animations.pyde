# Focus Learning: Python Level 1 Cont
# Animations
# Kavan Lam
# Dec 4, 2020


# Contents
# 1) Simple animation of a ball moving to the right
# 2) Animation of a ball moving up and down (bouncing off walls)
# 3) Same as 2 but with a square
# 4) Be able to switch the direction of animation with mouse pressed
# 5) Keep track of number of bounces and display on the screen

"""
# Section 1
x = 100
y = 300
def setup():
    size(900, 900)

def draw():
    global x
    global y
    background(0, 0, 0)
    
    fill(255, 0, 0)
    ellipse(x, y, 50, 50)
    
    # move the circle
    x = x + 10
"""    

"""
# Section 2
x = 450
y = 450
direction = 1  # Either 1 or -1 ---> 1 = move down , -1 = move up

def setup():
    size(900, 900)

def draw():
    global x
    global y
    global direction 
    
    background(0, 0, 0) # Remove the previous frame
    
    fill(255, 0, 0)
    ellipse(x, y, 50, 50)
    
    # move the circle
    y = y + (direction * 10)
    
    # Check for collision
    if y <= 0:
        direction = 1
    elif y >= 900:
        direction = -1
"""

"""
# Section 3
x = 450
y = 450
direction = 1  # Either 1 or -1 ---> 1 = move down , -1 = move up

def setup():
    size(900, 900)

def draw():
    global x
    global y
    global direction 
    
    background(0, 0, 0) # Remove the previous frame
    
    fill(255, 0, 0)
    rect(x, y, 50, 50)
    
    # move the circle
    y = y + (direction * 5)
    
    # Check for collision
    if y <= 0:
        direction = 1
    elif y >= 850:
        direction = -1
"""

# Section 4
x = 450
y = 450
direction = 1  # Either 1 or -1 ---> 1 = move down , -1 = move up
case = 1 # Either 1 or 2 --> 1 = Move up and down and 2 = move left and right

def setup():
    size(900, 900)

def draw():
    global x
    global y
    global direction 
    global case
    
    background(0, 0, 0) # Remove the previous frame
    
    fill(255, 0, 0)
    ellipse(x, y, 50, 50)
    
    # move the circle
    if case == 1:
        y = y + (direction * 10)
    elif case == 2:
        x = x + (direction * 10)
    
    # Check for collision
    if x <= 0:
        direction = 1
    elif x >= 900:
        direction = -1
        
    if y <= 0:
        direction = 1
    elif y >= 900:
        direction = -1

def mousePressed():
    global case
    
    if case == 1:
        case = 2
    elif case == 2:
        case = 1
    






























# Section 1
"""
x_pos = 100
y_pos = 300

def setup():
    size(900, 600)
    background(0, 0, 0)

def draw():
    global x_pos
    global y_pos
    
    background(0, 0, 0)
    
    fill(255, 0, 0)
    ellipse(x_pos, y_pos, 50, 50)
    
    # Move the circle
    x_pos = x_pos + 10
"""

# Section 2
"""
x_pos = 100
y_pos = 300
direction = 1

def setup():
    size(900, 600)
    background(0, 0, 0)

def draw():
    global x_pos
    global y_pos
    global direction
    
    background(0, 0, 0)
    
    fill(255, 0, 0)
    ellipse(x_pos, y_pos, 50, 50)
    
    # Move the circle
    y_pos = y_pos + (5 * direction)
    
    # Check for the ball bouncing
    if y_pos >= 560:
        direction = -1
    elif y_pos <= 40:
        direction = 1
"""

# Section 3
"""
x_pos = 100
y_pos = 300
direction = 1

def setup():
    size(900, 600)
    background(0, 0, 0)

def draw():
    global x_pos
    global y_pos
    global direction
    
    background(0, 0, 0)
    
    fill(255, 0, 0)
    rect(x_pos, y_pos, 50, 50)
    
    # Move the circle
    y_pos = y_pos + (5 * direction)
    
    # Check for the ball bouncing
    if y_pos >= 560:
        direction = -1
    elif y_pos <= 0:
        direction = 1
"""

"""
# Section 4/5
x_pos = 100
y_pos = 300
direction = 1
mouse_clicked = False
num_of_bounces = 0

def setup():
    global font1
    
    size(900, 600)
    background(0, 0, 0)
    font1 = loadFont("Jokerman-Regular-48.vlw")

def draw():
    global x_pos
    global y_pos
    global direction
    global mouse_clicked
    global num_of_bounces
    global font1
    
    background(0, 0, 0)
    
    fill(255, 0, 0)
    ellipse(x_pos, y_pos, 50, 50)
    
    textFont(font1, 25)
    fill(255, 255, 0)
    text("Number of bounces: " + str(num_of_bounces), 50, 50)
    
    # Move the circle
    if mouse_clicked == False:
        y_pos = y_pos + (5 * direction)
    else:
        x_pos = x_pos + (5 * direction)
    
    # Check for the ball bouncing
    if y_pos >= 560 or x_pos >= 850:
        direction = -1
        num_of_bounces = num_of_bounces + 1
    elif y_pos <= 40 or x_pos <= 40:
        direction = 1
        num_of_bounces = num_of_bounces + 1

def mousePressed():
    global mouse_clicked
    
    if mouse_clicked == False:
        mouse_clicked = True
    else:
        mouse_clicked = False
        
"""        
        
        
        
    

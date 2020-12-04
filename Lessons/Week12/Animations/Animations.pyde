# Focus Learning: Python Level 1 Cont
# Animations
# Kavan Lam
# Nov 4, 2020


# Contents
# 1) Simple animation of a ball moving to the right
# 2) Animation of a ball moving up and down (bouncing off walls)
# 3) Same as 2 but with a square
# 4) Be able to switch the direction of animation with mouse pressed
# 5) Keep track of number of bounces and display on the screen

































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
        
        
        
    

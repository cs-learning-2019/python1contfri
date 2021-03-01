# Focus Learning: Python Level 1 Cont
# Shoot Them Circles
# Kavan Lam
# Jan 8, 2021


# Homework
"""
1) Program the S and D keys to allow character to move right and down and make sure the character can't leave the screen
2) Go review Lesson 14
"""

# Steps
# 1) Setup the screen  [Done]
# 2) Create the character (for now it will be a sqaure) and making it move using WASD (ensure that it does not leave the screen)
# 3) Allow the chracter to shoot. Make a yellow laser.
# 4) Spawn the circles (bad guys)

character_size = 100
character_x = 400
character_y = 400
character_speed = 10

def setup():
    size(900, 900)


def draw():
    global character_size
    global character_x
    global character_y
    
    # Clear the screen/previous frame
    background(0, 0, 0)
    
    # Draw the character
    rect(character_x, character_y, character_size, character_size)
    
    # Draw the lasers (We will do this later)

def mousePressed():
    global character_x
    global character_y
    
    pushStyle()
    stroke(255, 255, 0)
    line(character_x, character_y, mouseX, mouseY)
    popStyle()
    

def keyPressed():
    global character_x
    global character_y
    global character_speed
    
    if key == "W" or key == "w":
        # The character should move up
        character_y = character_y - character_speed
        if character_y < 0:
            character_y = 0
    elif key == "A" or key == "a":
        # The character should move left
        character_x = character_x - character_speed
        if character_x < 0:
            character_x = 0
    # You need to program the other two keys
    



    
    

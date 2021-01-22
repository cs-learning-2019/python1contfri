# Focus Learning: Python Level 1 Cont
# Shoot Them Circles
# Kavan Lam
# Jan 8, 2021


# Homework
"""
1) There is this werid issue where I can kill circles when I do not even click on it. Fix it.
"""

# Steps
# 1) Setup the screen  [Done]
# 2) Create the character (for now it will be a sqaure) and making it move using WASD (ensure that it does not leave the screen) [Done]
# 3) Allow the chracter to shoot. Make a yellow laser. [Done]
# 4) Spawn the circles (bad guys) [Done]
# 5) Make the circles go towards the character [Done]
# 6) The circles need to die when I shoot them

character_size = 100
character_x = 400
character_y = 400
character_speed = 10

circle_x = []
circle_y = []
circle_spawn_time = 100

def setup():
    size(900, 900)

def draw():
    global character_size
    global character_x
    global character_y
    global circle_x
    global circle_y
    global circle_spawn_time
    
    # Clear the screen/previous frame
    background(0, 0, 0)
    
    # Draw the character
    rect(character_x, character_y, character_size, character_size)
    
    # Spawn a circle
    circle_spawn_time = circle_spawn_time - 1
    if circle_spawn_time == 0:
        temp_x = int(random(100, 800))
        temp_y = int(random(100, 800))
        circle_x.append(temp_x)
        circle_y.append(temp_y)
        circle_spawn_time = 100
    
    # Draw the circles
    for index in range(0, len(circle_x)):
        ellipse(circle_x[index], circle_y[index], 40, 40)
        
    # Move the cirlces (hint: you need to loop over all the circle just like we did above)
    new_circle_x = []
    new_circle_y = []
    for index in range(0, len(circle_x)):
        x_difference = character_x - circle_x[index]
        y_difference = character_y - circle_y[index]
        
        if x_difference > 0:
            x_difference = 1
        elif x_difference < 0:
            x_difference = -1
        
        if y_difference > 0:
            y_difference = 1
        elif y_difference < 0:
            y_difference = -1
        
        new_circle_x.append(circle_x[index] + x_difference)
        new_circle_y.append(circle_y[index] + y_difference)
    
    circle_x = new_circle_x
    circle_y = new_circle_y
        
        
    
def mousePressed():
    global character_x
    global character_y
    global circle_x
    global circle_y
    
    pushStyle()
    stroke(255, 255, 0)
    line(character_x + character_size / 2, character_y + character_size / 2, mouseX, mouseY)
    popStyle()
    
    # Detect to see if we hit a circle
    alive_circle_x = []
    alive_circle_y = []
    for index in range(0, len(circle_x)):
        # Check to see if this circle is bye bye
        if mouseX >= circle_x[index] - 40 and mouseX <= circle_x[index] + 40:
            if mouseY >= circle_y[index] - 40 and mouseY <= circle_y[index] + 40:
                # The circle is dead we got it!!!
                # Just do nothing
                pass
        else:
            alive_circle_x.append(circle_x[index])
            alive_circle_y.append(circle_y[index])
        
    
    circle_x = alive_circle_x
    circle_y = alive_circle_y
    
    
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
    elif key == "S" or key == "s":
        # The character should move down
        character_y = character_y + character_speed
        if character_y > 800:
            character_x = 800
    elif key == "D" or key == "d":
        # The character should move right
        character_x = character_x + character_speed
        if character_x > 800:
            character_x = 800

    



    
    

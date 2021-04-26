# Focus Learning: Python Level 1 cont 
# PONG
# Kavan Lam
# April 19, 2021

###### HOMEWORK ######
# 1) Make the ball bounce off of player 2
# 2) Make the ball bonuce off the top and bottom wall as well

player1_x = 50
player1_y = 220
player1_speed = 15

player2_x = 950
player2_y = 220
player2_speed = 15

ball_x = 500
ball_y = 300
ball_speed = 3
ball_direction = [-1, 0]
ball_size = 30

def setup():
    size(1000, 600)

def draw():
    global player1_x
    global player1_y
    
    global player2_x
    global player2_y
    
    global ball_x
    global ball_y
    global ball_speed
    global ball_direction
    global ball_size
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the center line
    pushStyle()
    stroke(255, 0, 0)
    line(500, 0, 500, 600)
    popStyle()
    
    # Draw player1
    pushStyle()
    strokeWeight(5)
    stroke(0, 0, 255)
    line(player1_x, player1_y, player1_x, player1_y + 100)
    popStyle()
    
    # Draw player2
    pushStyle()
    strokeWeight(5)
    stroke(0, 0, 255)
    line(player2_x, player2_y, player2_x, player2_y + 100)
    popStyle()
    
    # Draw the ball
    pushStyle()
    fill(255, 255, 0)
    ellipse(ball_x, ball_y, ball_size, ball_size)
    popStyle()
    
    # Move the ball
    ball_x = ball_x + ball_speed * ball_direction[0]
    ball_y = ball_y + ball_speed * ball_direction[1]
    
    # Detect the ball hitting the player 1 paddle
    if (ball_y >= player1_y and ball_y <= player1_y + 100) and (ball_x >= player1_x - 5 and ball_x <= player1_x + 5):
        if ball_direction[0] == -1:
            ball_direction[0] = 1
        elif ball_direction[0] == 1:
            ball_direction[0] = -1
        
        ball_direction[1] = random(-1, 1)
                
def keyPressed():
    global player1_y
    global player1_speed
    
    global player2_y
    global player2_speed
    
    
    # Player 1
    if key == "W" or key == "w": # Move up
        player1_y = player1_y - player1_speed
        if player1_y < 0:
            player1_y = 0
    elif key == "S" or key == "s": # Move down
        player1_y = player1_y + player1_speed
        if player1_y > 500:
            player1_y = 500

    # Player 2
    if keyCode == UP: # Move up
        player2_y = player2_y - player2_speed
        if player2_y < 0:
            player2_y = 0
    elif keyCode == DOWN: # Move down
        player2_y = player2_y + player2_speed
        if player2_y > 500:
            player2_y = 500

    
    
    
    
    
    

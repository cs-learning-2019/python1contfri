# Focus Learning: Python Level 1 cont 
# PONG
# Kavan Lam
# May 10, 2021

###### HOMEWORK ######
# NO HOMEWORK

###### TODO #######
# 1) The game does not end (Game over screen) (with a reset button)

add_library("minim")
game_music_on = False
game_over_music_on = False

scene = 1  # 0 -> Main Menu   1 -> Game    2 -> Game Over
max_score = 1
winning_player = 0  # 0 -> Do not know   1 -> Player 1 won   2 -> Player 2 won

player1_x = 50
player1_y = 220
player1_speed = 15
player1_score = 0

player2_x = 950
player2_y = 220
player2_speed = 15
player2_score = 0

ball_x = 500
ball_y = 300
ball_speed = 2
ball_direction = [1, 0]
ball_size = 30

def setup():
    global my_game_music
    global my_other_music
    global minim
    
    size(1000, 600)
    
    minim = Minim(this) # We are creating a dvd player a putting it into minim variable
    my_game_music = minim.loadFile("game_music.mp3")
    my_other_music = minim.loadFile("music2.mp3")

def draw():
    global scene
    
    if scene == 1:
        draw_game()
    elif scene == 2:
        draw_game_over()
    
def draw_game_over():
    global winning_player
    global game_music_on
    global game_over_music_on
    global my_other_music
    global minim
    
    background(0, 255, 0)
    textAlign(CENTER)
    fill(255, 0, 0)
    textSize(40)
    text("Game Over", 500, 300)
    
    if winning_player == 1:
        text("Player 1 has won", 500, 400)
    elif winning_player == 2:
        text("Player 2 has won", 500, 400)
    
    game_music_on = False
    if game_over_music_on == False:
        minim.stop()
        my_other_music = minim.loadFile("music2.mp3")
        my_other_music.loop()
        game_over_music_on = True
    
def draw_game():
    global player1_x
    global player1_y
    global player1_score
    
    global player2_x
    global player2_y
    global player2_score
    
    global ball_x
    global ball_y
    global ball_speed
    global ball_direction
    global ball_size
    
    global scene
    global max_score
    global winning_player
    global my_game_music
    global game_music_on
    global game_over_music_on
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # play music
    game_over_music_on = False
    if game_music_on == False:
        my_game_music.loop()
        game_music_on = True
    
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
    
    # Detect the ball hitting the player 1 paddle and bounce
    if (ball_y >= player1_y and ball_y <= player1_y + 100) and (ball_x >= player1_x - 5 and ball_x <= player1_x + 5):
        if ball_direction[0] == -1:
            ball_direction[0] = 1
        elif ball_direction[0] == 1:
            ball_direction[0] = -1
        
        ball_direction[1] = random(-1, 1)
        ball_speed += 1
        
    # Detect the ball hitting the player 2 paddle and bounce
    if (ball_y >= player2_y and ball_y <= player2_y + 100) and (ball_x >= player2_x - 5 and ball_x <= player2_x + 5):
        if ball_direction[0] == -1:
            ball_direction[0] = 1
        elif ball_direction[0] == 1:
            ball_direction[0] = -1
        
        ball_direction[1] = random(-1, 1)
        ball_speed += 1
        
    # Detect the ball hitting the top wall
    if (ball_y <= ball_size - 15):
        ball_direction[1] = random(0, 1)
        
    # Detect the ball hitting the bottom wall
    if (ball_y >= 600 - 15):
        ball_direction[1] = random(-1, 0)
    
    # Draw player 1 score
    pushStyle()
    textSize(25)
    fill(0, 255, 0)
    text(player1_score, 50, 50)
    popStyle()
    
    # Draw player 2 score
    pushStyle()
    textSize(25)
    fill(0, 255, 0)
    text(player2_score, 950, 50)
    popStyle()
    
    # Detect the ball hitting the right wall (player 1 has scored)
    if ball_x >= 1000:
        player1_score = player1_score + 1
        ball_x = 500
        ball_y = 300
        ball_speed = 2
        ball_direction = [-1, 0]
        
    # Detect the ball hitting the left wall (player 2 has scored)
    if ball_x <= 0:
        player2_score = player2_score + 1
        ball_x = 500
        ball_y = 300
        ball_speed = 2
        ball_direction = [1, 0]
    
    # Check to see if any player has reached the max score
    if player1_score == max_score:
        scene = 2 
        winning_player = 1
    elif player2_score == max_score:
        scene = 2 
        winning_player = 2

                
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

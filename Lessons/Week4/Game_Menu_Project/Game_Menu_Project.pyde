# Focus Learning: Python Level 1 cont
# Game Menu Project
# Kavan Lam
# Oct 3, 2020 

def setup():
    global mario
    
    size(1000, 800)
    mario = loadImage("Mario.png")
    
    
def draw():
    background(0, 0, 0)
    
    # Title
    pushStyle()
    fill(255, 0, 0)
    textSize(50)
    textAlign(CENTER)
    text("Focus Learning", 500, 50)
    popStyle()
    
    # Play Button
    pushStyle()
    fill(0, 255, 0)
    rect(100, 400, 200, 100)
    fill(0, 0, 255)
    textSize(40)
    textAlign(CENTER)
    text("Play", 200, 460)
    popStyle()
    
    # Quit Button
    pushStyle()
    fill(0, 255, 0)
    rect(400, 400, 200, 100)
    fill(0, 0, 255)
    textSize(40)
    textAlign(CENTER)
    text("Quit", 500, 460)
    popStyle()
    
    # Mario Picture
    pushStyle()
    image(mario, 400, 100, 150, 300)
    popStyle()
    
    
    
    
    

# Focus Learning: Python Level 1 Cont
# Review of Processing
# Kavan Lam
# Sept 25, 2020

def setup():
    global font1
    global pic1
    
    size(900, 600)
    font1 = loadFont("BodoniMTBlack-48.vlw")
    pic1 = loadImage("mario.png")

def draw():
    global font1
    global pic1
    
    background(0, 0, 255)  # We use RGB colors and each number is from 0 to 255
    fill(255, 255, 0)
    stroke(255, 0, 0) # stroke is for the border of the shape
    rect(200, 450, 50, 50)
    line(50, 50, 400, 400)
    point(500, 500)  # We need to use strokeWeight to make it bigger
    
    pushStyle()
    fill(0, 255, 0)
    stroke(255, 255, 0)
    strokeWeight(6)
    ellipse(300, 250, 100, 100)
    popStyle()
    
    pushStyle()
    fill(255, 0, 0)
    textFont(font1) # This will also set your font size to 48
    textSize(100)  # Change the font size
    text("Hello", 50, 100)
    popStyle()
    
    
    image(pic1, 200, 350, 200, 200)
    
    
    
    

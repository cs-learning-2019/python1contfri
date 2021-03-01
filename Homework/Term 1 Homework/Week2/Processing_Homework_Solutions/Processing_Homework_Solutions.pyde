# Focus Learning Python Level 1 Cont
# Processing shapes, sounds and text homework solutions
# Kavan Lam
# Sept 13, 2020

# Question 1
"""
The dot will appear in the top-left corner of the output screen
"""

# Question 2
"""
We can use the strokeWeight() function to change how big the dot/point is. Eg/ strokeWeight(5)
We can use the stroke() function to change the color of the dot Eg/ stroke(255, 0, 0)
"""

# Question 3
"""
The fill() function will not work on lines and dots because fill() only works on 2D shapes
like rectangles, squares and circles.
"""

# Question 4
"""
Minim is a library that you can add to you Processing project so that we can play sound
files. One sound file type is .mp3 another one is .wav.
"""

# Question 5
def setup():
    size(900, 600)
    background(0, 0, 0)
    
def draw():
    # Draw the circle
    fill(255, 255, 0)
    ellipse(450, 300, 400, 400)
    
    # Draw the rectangles
    fill(255, 0, 0)
    rect(300, 200, 50, 50)
    rect(400, 200, 50, 50)
    rect(300, 300, 50, 50)
    rect(350, 400, 50, 50)
    
    # Draw the text
    textSize(30)
    text("Some cool abstract art", 300, 50)
    

# Focus Learning: Intro to Processing part 2
# Sounds in Processing
# Kavan Lam
# Oct 2, 2020

# Add the Minim library
add_library("minim")  # add_library  --> that is a function 
# To be clear a function will always have the ()  after the name
first_time = True

def setup():
    global minim
    global tick
    global song
    
    size(900, 600)
    minim = Minim(this) # We are creating a dvd player a putting it into minim
    song = minim.loadFile("song.mp3") 
    tick = minim.loadFile("Tick.wav") 
    
    # song.loop()  we are already playing the song in the draw section
    # Note you can do this  minim.loadFile("song.mp3").loop()  this will load and play in 1 line of code


def draw():
    global first_time
    
    rect(100, 100, 200, 200)
    
    if first_time == True:
        song.loop()  # loop has a built in rewind
        first_time = False

def mousePressed():
    tick.play()
    tick.rewind()
    

def keyPressed():
    global minim
    global song
    global tick
    
    if key == "P" or key == "p":
        song = minim.loadFile("song.mp3")
        tick = minim.loadFile("Tick.wav")
        song.loop()
    elif key == "S" or key == "s":
        # Stop song
        minim.stop() # Kills your dvd player so now you can never play sound effects unless..... you reload your sound effect
    

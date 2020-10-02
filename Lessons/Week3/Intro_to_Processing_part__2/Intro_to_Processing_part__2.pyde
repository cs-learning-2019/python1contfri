# Focus Learning: Intro to Processing part 2
# Sounds in Processing
# Kavan Lam
# Sept 26, 2020

# Add the Minim library
add_library("minim")  # add_library  --> that is a function 
# To be clear a function will always have the ()  after the name

def setup():
    global minim
    global song
    global tick
    
    size(900, 600)
    minim = Minim(this)  # We are creating a dvd player a putting it into minim
    song = minim.loadFile("song.mp3")
    tick = minim.loadFile("Tick.wav")
    
    song.loop()
    # Note you can do this  minim.loadFile("song.mp3").loop()  this will load and play in 1 line of code
    

def draw():
    background(0, 0, 255)
    rect(100, 100, 50, 50)


def mousePressed():
    global tick
    print("You pressed your mouse")
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
    elif key == "S" or "s":
        # Stop song
        minim.stop() # Kills your dvd player so now you can never play sound effects unless..... you reload your sound effect
    
    
    
    
    
    

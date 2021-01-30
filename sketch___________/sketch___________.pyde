def setup():
    size(600,480)
    frameRate(1)
def draw():
    background(255)
    strokeWeight(10)
    stroke(random(0,255),random(0,255),random(0,255))
    for s in range (0,100):
        point(random(0,600),random(0,480))
    

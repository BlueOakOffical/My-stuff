def setup():
    frameRate(10)
    size(1800,1080)
def draw():
    background(255)
    fill(255,0,0)
    for s in range (0,10000):
        rect(random(1800),random(1080),20,20)
        text("ERROR",random(1800),random(1080))
        text("0101010110101",random(1800),random(1080))                                     

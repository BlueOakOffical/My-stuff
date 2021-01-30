def setup():
    size(600,480)
def draw():
    if keyPressed:
        fill(132,32,132)
        rect(300,240,10,30)
        rect(150,240,10,30)
    else:
        fill(0)
        rect(300,240,10,30)
    if mousePressed:
        fill(255,0,0)
        rect(150,240,10,30)
    else:
        fill(0)
        rect(150,240,10,30)
        

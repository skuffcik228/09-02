def setup():
    size(600,400)
    background(0)
def draw():
    frameRate(10)
    fill(random(0, 255),random(0,255),random(0,255))
    ellipse(random(1,600), random(1,400),random(1,20),10)
    

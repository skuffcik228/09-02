def setup():
    size(600,400)
    fill(0)
    ellipse(150,300,50,50)
    translate(50,290)
    rotate(radians(-40))
    rect(0,0,150,50)
def draw():
    fill(random(1,255),random(1,255),random(1,255))
    rect(random(250,600),random(1,200),random(5,10),random(5,10))
    

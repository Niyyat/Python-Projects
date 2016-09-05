import turtle

class Star():
    def __init__(self,x,y,arm_length,color):
        self.x=x
        self.y=y
        self.arm_length=arm_length
        self.color=color
    def draw(self,a):
        star_pos_x=self.x+self.arm_length/3.236
        star_pos_y=self.y+self.arm_length/2.3511
        a=turtle.Turtle()
        a.setpos(star_pos_x,star_pos_y)
        for i in range(5):
            a.forward(self.arm_length)
            a.right(144)
            a.forward(self.arm_length)
            a.left(72)
    def __str__(self):
        return 'Star x:'+str(self.x)+', y:' + str(self.y)+ ', arm:' +str(self.arm_length) + ', color:' + str(self.color)


c=Star(-200,100,400,"red")
d=turtle.Turtle()
Star.draw(d)

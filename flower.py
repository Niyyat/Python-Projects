import turtle

def flower():
    window=turtle.Screen()
    window.bgcolor("yellow")
    gul=turtle.Turtle()
    gul.shape("turtle")
    gul.color("green")
    gul.speed(10)

    for i in range(80):
        gul.left(85)
        gul.forward(100)
        gul.right(170)
        gul.forward(100)
    gul.home()
    
    gul.right(90)
    gul.forward(300)
    gul.left(90)
    gul.forward(10)
    gul.left(90)
    gul.forward(100)
    gul.right(50)
    gul.forward(90)
    gul.left(150)
    gul.forward(70)
    gul.right(100)
    gul.forward(140)
    
    

    window.exitonclick()
flower()

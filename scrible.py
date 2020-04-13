import turtle as t

window= t.Screen()
window.bgcolor("white")
window.setup(width=800,height=600)

brush=t.Turtle()
brush.shape("square")
brush.shapesize(stretch_len=0.3, stretch_wid=0.3)
brush.goto(0,0)
brush.pen()
brush.dx=0.6
brush.dy=0.6


def up():
    a = 1
    b = 0
    c = 0
    d = 0
    while a==1:
        brush.sety(brush.ycor() + brush.dy)

def down():
    a = 0
    b = 1
    c = 0
    d = 0
    while b==1:
        brush.sety(brush.ycor() - brush.dy)

def left():
    a = 0
    b = 0
    c = 1
    d = 0
    while c==1:
        brush.setx(brush.xcor() - brush.dx)

def right():
    a = 0
    b = 0
    c = 0
    d = 1
    while d==1:
        brush.setx(brush.xcor() + brush.dx)


window.listen()
window.onkeypress(up,"Up")
window.onkeypress(down,"Down")
window.onkeypress(right,"Right")
window.onkeypress(left,"Left")






while True:
    window.update()





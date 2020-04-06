import turtle as t

wn= t.Screen()
wn.title("My PingPong Game")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


paddle_a= t.Turtle()
paddle_a.speed(0)
paddle_a.shape("circle")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-375,0)

paddle_b= t.Turtle()
paddle_b.speed(0)
paddle_b.shape("circle")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(375,0)

ball= t.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.shapesize(stretch_len=0.7, stretch_wid=0.7)
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1


def p_a_up():
    y= paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def p_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def p_b_up():
    y= paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def p_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



wn.listen()
wn.onkeypress(p_a_up,"w")
wn.onkeypress(p_a_down,"s")
wn.onkeypress(p_b_up,"Up")
wn.onkeypress(p_b_down,"Down")


while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if( ball.ycor()> 290 ):
        ball.sety(290)
        ball.dy *= -1
    if (ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1
    if ( ball.xcor()>390 ):
        ball.goto(0,0)
        ball.dx *= -1
    if ( ball.xcor()<-390 ):
        ball.goto(0,0)
        ball.dx *= -1

    if( ball.xcor()> 370 and ball.xcor()<380 and ball.ycor()< paddle_b.ycor()+50 and ball.ycor()> paddle_b.ycor()-50):
        ball.setx(370)
        ball.dx *= -1
    if (ball.xcor() < -370 and ball.xcor() > -380 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-370)
        ball.dx *= -1


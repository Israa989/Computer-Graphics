import turtle
def square(t,length):
    color=['yellow','blue','red','green']
    for i in range(15):
        for j in range(4):
         t.color(color[j])
         t.fd(length)
         t.lt(90)
        t.penup()
        t.goto(i-(length-i),i-(length-i))
        t.pendown()
        length+=5
m=turtle.Turtle()
square(m,0)
turtle.done()
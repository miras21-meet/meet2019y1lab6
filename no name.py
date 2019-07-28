Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5%3
2
>>> import turtle
turtle.tracer(1)
rounds = 10
size = 10
mike = turtle.clone()
steve = turtle.clone()
turtle.bgcolor("white")
turtle.hideturtle()
mike.color("gold")
steve.color("blue")
steve.goto(5,5)
while True:
    mike.forward(size)
    mike.left(90)
    steve.forward(-size)
    steve.left(-90)
    size += 10
turtle.mainloop()

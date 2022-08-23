from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
tt = Turtle()
tt.pen()
tt.shape('arrow')
tt.speed('fastest')
tt.pu()

color_list = [(236, 35, 108), (222, 231, 237), (145, 28, 65), (239, 74, 34), (6, 148, 93), (231, 238, 234), (232, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93),
              (172, 36, 98), (246, 219, 44), (42, 172, 112), (216, 130, 165), (216, 58, 26)]


def random_color():
    color = random.choice(color_list)
    return (color)


x = -250
y = -250
for w in range(10):
    for i in range(10):
        tt.setpos(x, y)
        color = random_color()
        tt.dot(20, color)
        x += 50
    x = -250
    y += 50
screen.exitonclick()

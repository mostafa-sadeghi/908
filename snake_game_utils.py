from turtle import Screen, Turtle


def make_screen():
    main_surface = Screen()
    main_surface.bgcolor('black')
    main_surface.setup(width=600, height=600)
    main_surface.title('Snake Game')
    main_surface.tracer(False)
    return main_surface


def make_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed('fastest')
    return my_turtle


def reset(head, tails):
    head.goto(0, 0)
    head.direction = ""
    for t in tails:
        t.ht()

    tails.clear()

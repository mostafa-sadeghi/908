from turtle import Screen, Turtle

# TODO def make_screen()
main_surface = Screen()
main_surface.bgcolor('black')
main_surface.setup(width=600, height=600)
main_surface.title('Snake Game')

def make_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed('fastest')
    return my_turtle

snake_body = make_turtle("square", "blue")
snake_body.setposition(100,100)


snake_food = make_turtle("circle", "red")
# TODO   جای غذا به صورت تصادفی تغییر


# Game Main loop
running = True
while running:
    main_surface.update()
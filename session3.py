from turtle import Screen, Turtle
from random import randint
from time import sleep

# TODO def make_screen()
main_surface = Screen()
main_surface.bgcolor('black')
main_surface.setup(width=600, height=600)
main_surface.title('Snake Game')
main_surface.tracer(False)


def make_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed('fastest')
    return my_turtle


def change_food_position():
    random_x = randint(-280, 280)
    random_y = randint(-280, 280)
    snake_food.goto(random_x, random_y)


def move_snake():
    if snake_head.direction == "up":
        ypos = snake_head.ycor()
        ypos += 20
        snake_head.sety(ypos)
    if snake_head.direction == "right":
        xpos = snake_head.xcor()
        xpos += 20
        snake_head.setx(xpos)
    # TODO حرکت به سمت پائین و نیز چپ

def go_up():
    snake_head.direction = "up"

# TODO اضافه کردن تابع برای سایر جهت ها

snake_head = make_turtle("square", "blue")
snake_head.setposition(100, 100)
snake_head.direction = ""


snake_food = make_turtle("circle", "red")
change_food_position()


main_surface.listen()
main_surface.onkeypress(go_up,"Up")
# TODO
# اضافه کردن رویداد برای سایر جهت ها


# Game Main loop
running = True
while running:
    main_surface.update()
    move_snake()
    sleep(0.2)

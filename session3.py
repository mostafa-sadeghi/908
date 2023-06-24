from random import randint
from time import sleep
from snake_game_utils import *

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
    if snake_head.direction == "down":
        ypos = snake_head.ycor()
        ypos -= 20
        snake_head.sety(ypos)

    if snake_head.direction == "left":
        xpos = snake_head.xcor()
        xpos -= 20
        snake_head.setx(xpos)


def go_up():
    snake_head.direction = "up"


def go_down():
    snake_head.direction = "down"


def go_left():
    snake_head.direction = "left"


def go_right():
    snake_head.direction = "right"


snake_head = make_turtle("square", "blue")
snake_head.setposition(100, 100)
snake_head.direction = ""


snake_food = make_turtle("circle", "red")
change_food_position()

main_surface = git
main_surface.listen()
main_surface.onkeypress(go_up, "Up")
main_surface.onkeypress(go_down, "Down")
main_surface.onkeypress(go_left, "Left")
main_surface.onkeypress(go_right, "Right")


# Game Main loop
running = True
while running:
    main_surface.update()
    move_snake()
    sleep(0.2)

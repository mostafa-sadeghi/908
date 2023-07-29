from random import randint
from time import sleep
from snake_game_utils import *

score = 0
high_score = 0


def change_food_position():
    random_x = randint(-280, 280)
    random_y = randint(-280, 230)
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
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


snake_head = make_turtle("square", "blue")
snake_head.setposition(100, 100)
snake_head.direction = ""

snake_food = make_turtle("circle", "red")
change_food_position()

score_board = make_turtle("square", "white")
score_board.hideturtle()
score_board.goto(0, 260)

main_surface = make_screen()
main_surface.listen()
main_surface.onkeypress(go_up, "Up")
main_surface.onkeypress(go_down, "Down")
main_surface.onkeypress(go_left, "Left")
main_surface.onkeypress(go_right, "Right")


def on_close():
    global running
    running = False


root = main_surface._root
root.protocol("WM_DELETE_WINDOW", on_close)

snake_tails = []

# Game Main loop
running = True
while running:
    score_board.clear()
    score_board.write(f"Score: {score}\tHighScore: {high_score}",
                      align="center",
                      font=("Tahoma", 22))
    main_surface.update()
    if snake_head.distance(snake_food) < 20:
        score += 1
        if score > high_score:
            high_score = score
        change_food_position()
        new_tail = make_turtle("square", "cyan")
        snake_tails.append(new_tail)

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        reset(snake_head, snake_tails)
        score = 0

    for i in range(len(snake_tails) - 1, 0, -1):
        prevx = snake_tails[i - 1].xcor()
        prevy = snake_tails[i - 1].ycor()
        snake_tails[i].setpos(prevx, prevy)

    if len(snake_tails) > 0:
        headx = snake_head.xcor()
        heady = snake_head.ycor()
        snake_tails[0].setpos(headx, heady)

    move_snake()
    for body in snake_tails:
        if body.distance(snake_head) < 20:
            reset(snake_head, snake_tails)
            score = 0
    sleep(0.2)

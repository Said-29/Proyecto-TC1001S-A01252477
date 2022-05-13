from turtle import *
from random import randrange
import turtle
from freegames import square, vector
import time

max_len = 1
def main():
    global start_time
    global time_left
    global max_len

    scoreboard = turtle.Turtle()
    scoreboard.hideturtle()
    scoreboard.penup()
    scoreboard.setposition(-180,190)
    scoreboard.color("white")
    scoreboard.write("Score: 1", move=False, align='center', font=('Times New Roman', 9, 'bold'))

    max_scoreboard = turtle.Turtle()
    max_scoreboard.hideturtle()
    max_scoreboard.penup()
    max_scoreboard.setposition(-170,170)
    max_scoreboard.color("white")
    max_scoreboard.write(f"Max score: {max_len}", move=False, align='center', font=('Times New Roman', 9, 'bold'))

    timer = turtle.Turtle()
    timer.hideturtle()
    timer.penup()
    timer.setposition(160,170)
    timer.color("white")
    timer.write(f"Time left: {time_left}", move=False, align='center', font=('Times New Roman', 9, 'bold'))

    food = vector(0, 0)
    snake = [vector(10, 0)]
    aim = vector(0, -10)

    def change(x, y):
        "Change snake direction."
        aim.x = x
        aim.y = y

    def inside(head):
        "Return True if head inside boundaries."
        return -200 < head.x < 190 and -200 < head.y < 190

    def move():
        global start_time
        global max_len
        global time_left
        "Move snake forward one segment."
        head = snake[-1].copy()
        head.move(aim)

        time_taken = round(time.time() - start_time)
        time_left = 10 - time_taken
        timer.clear()
        timer.write(f"Time left: {time_left}", move=False, align='center', font=('Times New Roman', 9, 'bold'))

        if not inside(head) or head in snake or time_left <= 0:
            square(head.x, head.y, 9, 'red')
            update()
            penup()
            setposition(0,50)
            write('PERDISTE :(' , move=False ,align='center',font=('Times New Roman',18,'bold'))
            max_scoreboard.clear()
            scoreboard.clear()
            if len(snake) > max_len:
                max_scoreboard.write(f"Max score: {len(snake)}", move=False, align='center', font=('Times New Roman', 9, 'bold'))
                max_len = len(snake)
            setposition(0,0)
            color('white')
            write('Click to play', move=False, align='center', font=('Times New Roman', 18, 'bold'))
            setposition(0,-25)
            write(f'Score: {len(snake)}', move=False, align='center', font=('Times New Roman', 18, 'bold'))
            time_taken = 0
            timer.clear()
            timer.write(f"Time left: {time_left}", move=False, align='center', font=('Times New Roman', 9, 'bold'))
            exitonclick()

        snake.append(head)

        if head == food:
            start_time = time.time()
            time_taken = 0
            time_left = 30
            timer.clear()
            timer.write(f"Time left: {time_left}", move=False, align='center', font=('Times New Roman', 9, 'bold'))
            scoreboard.clear()
            scoreboard.write(f"Score: {len(snake)}", move=False, align='center', font=('Times New Roman', 9, 'bold'))
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10
        else:
            snake.pop(0)

        clear()

        for body in snake:
            square(body.x, body.y, 9, 'green')

        square(food.x, food.y, 9, 'red')
        update()
        ontimer(move, 100)

    window = turtle.Screen()
    window.title("Snake Game")
    window.bgcolor("black")
    window.setup(420, 420, 370, 0)
    window.tracer(0)

    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    move()
    done()

while True:
    start_time = time.time()
    time_left = 10
    main()





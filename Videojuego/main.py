#Jordan Barba
#A01252477
#TC1001S
#Evidencia Semana Tec

#Librerias
from turtle import *
from random import randrange
import turtle
from freegames import square, vector
import time

#Jimena Gallegos
#High score incial
max_len = 1

def main():
    #Variables globales
    global start_time
    global time_left
    global max_len

    #Jimena Gallegos
    #Objeto turtle con el score actual
    scoreboard = turtle.Turtle()
    scoreboard.hideturtle()
    scoreboard.penup()
    scoreboard.setposition(-180,190)
    scoreboard.color("white")
    scoreboard.write("Score: 1", move=False, align='center', font=('Times New Roman', 9, 'bold'))

    #Jimena Gallegos
    #Objeto turtle con el score maximo
    max_scoreboard = turtle.Turtle()
    max_scoreboard.hideturtle()
    max_scoreboard.penup()
    max_scoreboard.setposition(-170,170)
    max_scoreboard.color("white")
    max_scoreboard.write(f"Max score: {max_len}", move=False, align='center', font=('Times New Roman', 9, 'bold'))

    #Jordan Barba
    #Objeto turtle con el cronometro
    timer = turtle.Turtle()
    timer.hideturtle()
    timer.penup()
    timer.setposition(160,170)
    timer.color("white")
    timer.write(f"Time left: {time_left}", move=False, align='center', font=('Times New Roman', 9, 'bold'))

    #Comida en forma de vector con la libreria freegames
    food = vector(0, 0)

    #Serpiente en forma de vector con la libreria freegames
    snake = [vector(10, 0)]

    #Direccion en forma de vector con la libreria freegames
    aim = vector(0, -10)

    def change(x, y):
        "Change snake direction."
        aim.x = x
        aim.y = y

    def inside(head):
        "Return True if head inside boundaries."
        return -200 < head.x < 190 and -200 < head.y < 190

    def move():
        #Variables globales
        global start_time
        global max_len
        global time_left

        "Move snake forward one segment."
        head = snake[-1].copy()
        head.move(aim)

        #Jordan Barba
        #Tiempo consumido desde la ultima vez que crecio la cabeza
        time_taken = round(time.time() - start_time)

        #Tiempo restante antes de perder
        time_left = 10 - time_taken

        #Actualizar el tiempo restante en pantalla
        timer.clear()
        timer.write(f"Time left: {time_left}", move=False, align='center', font=('Times New Roman', 9, 'bold'))

        #Derrota al momento de chocar con la pared, contra el cuerpo de la serpiente, o si se acaba el tiempo
        if not inside(head) or head in snake or time_left <= 0:
            square(head.x, head.y, 9, 'red')
            update()
            
            #Pablo Martinez
            #Aviso de perdiste en el centro de la pantalla
            penup()
            setposition(0,50)
            write('PERDISTE :(' , move=False ,align='center',font=('Times New Roman',18,'bold'))

            #Jimena Gallegos
            #Limpiar ambos scoreboards, para posteriormente actualizarlos
            max_scoreboard.clear()
            scoreboard.clear()

            #Si hay un nuevo high score actualizarlo
            if len(snake) > max_len:
                max_scoreboard.write(f"Max score: {len(snake)}", move=False, align='center', font=('Times New Roman', 9, 'bold'))
                max_len = len(snake)

            #Pablo Martinez
            #Volver a jugar
            setposition(0,0)
            color('white')
            write('Click to play', move=False, align='center', font=('Times New Roman', 18, 'bold'))

            #Jimena Gallegos
            #Mostrar score
            setposition(0,-25)
            write(f'Score: {len(snake)}', move=False, align='center', font=('Times New Roman', 18, 'bold'))

            #Jordan Barba
            #Reiniciar temporizador
            time_taken = 0
            timer.clear()
            timer.write(f"Time left: {time_left}", move=False, align='center', font=('Times New Roman', 9, 'bold'))

            #Pablo Martinez
            #Terminar partida al hacer click
            exitonclick()

        #Añade una parte a la serpiente
        snake.append(head)

        #Detectar cuando la serpiente este en la posicion de la comida
        if head == food:
            #Jordan Barba
            #Variables de tiempo
            start_time = time.time()
            time_taken = 0
            time_left = 10
            timer.clear()
            timer.write(f"Time left: {time_left}", move=False, align='center', font=('Times New Roman', 9, 'bold'))

            #Jimena Gallegos
            #Actualizar score
            scoreboard.clear()
            scoreboard.write(f"Score: {len(snake)}", move=False, align='center', font=('Times New Roman', 9, 'bold'))

            #Colocar comida nueva
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10
        else:
            snake.pop(0)

        clear()

        #Dibujar serpiente
        for body in snake:
            square(body.x, body.y, 9, 'green')

        #Dibujar comida
        square(food.x, food.y, 9, 'red')
        update()
        ontimer(move, 100)

    #Pablo Fong
    #Objeto turtle de pantalla
    window = turtle.Screen()
    window.title("Snake Game")
    window.bgcolor("black")
    window.setup(420, 420, 370, 0)
    window.tracer(0)

    #Pablo Fong
    #Especifiaciones de turtle
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    move()
    done()

#Pablo Martinez
#Continuar hasta que el usuario deje de jugar
while True:
    #Variables iniciales de tiempo
    start_time = time.time()
    time_left = 10
    main()
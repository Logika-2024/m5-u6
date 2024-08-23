from turtle import *
from time import sleep

# Поле гри
speed(10)
penup()
goto(-110, 110)
pendown()
for i in range(4):
    forward(220)
    right(90)

# створимо напис для життів гравця
lives_board = Turtle()
lives_board.color("blue")
lives_board.penup()
lives_board.goto(-100, 120)

class Sprite(Turtle):
    def start_pos_shape_color(self, x, y, sh, col):
        self.shape(sh)
        self.color(col)
        self.penup()
        self.goto(x, y)

    def make_step(self, step):
        # якщо дойшли до краю поля,
        x = self.xcor()
        if x < -90 or x > 90:
        #if not (-100 <= x <= 100):
            self.speed(10)
            self.left(180)
            self.speed(2)
        self.forward(step)

    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 20:
            return True
        else:
            return False

# Створюємо об'єкти перешкоди з позиціями

block_left = Sprite()
block_left.start_pos_shape_color(-90, 30, "square", "red")

block_right = Sprite()
block_right.start_pos_shape_color(90, -50, "square", "red")

# Створюємо об'єкт фініш

finish = Sprite()
finish.start_pos_shape_color(0, 100, "triangle", "green")

# Об'єкт гравця

main = Turtle()
main.shape("circle")
main.color("orange")
main.penup()
main.goto(0, -100)
main.lives = 3

score_font = ("Roboto", 14, "bold")
lives_board.write("Lives: " + str(main.lives), font=score_font)


# Зробимо обробник подій для спрайта гравця

def go_up():
    # print("go up, x:")
    main.goto(main.xcor(), main.ycor() + 10)
def go_down():
    #print("go down")
    main.goto(main.xcor(), main.ycor() - 10)
def go_left():
    #print("go left")
    main.goto(main.xcor()-10, main.ycor())
def go_right():
    #print("go right")
    main.goto(main.xcor()+10, main.ycor())

# Задаємо слухачі подій на натискання кнопок (стрілок)

screen = main.getscreen()
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")


# Запускаємо гру !!!

while main.lives > 0:
    block_left.make_step(10)
    block_right.make_step(5)

    # Перевірка, якщо дійшли до фініша
    if finish.is_collide(main):
        block_left.hideturtle()
        block_right.hideturtle()
        break
    # Перевірка на зіткнення
    if block_left.is_collide(main) or block_right.is_collide(main):
        sleep(1)
        main.write("you loose", font=("Roboto", 12, "normal"))
        sleep(1)
        main.clear()
        main.lives -= 1
        lives_board.clear()
        if main.lives > 0:
            lives_board.write("Lives: " + (main.lives), font=score_font)
            main.goto(0, -100)
        else:
            lives_board.hideturtle()

# По завершенню цикла
if main.lives == 0:
    write("You Lost the game !", font=score_font)
else:
    color("orange")
    write("You Win !!!", font=score_font)

exitonclick()

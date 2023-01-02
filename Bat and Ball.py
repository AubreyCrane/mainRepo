import tkinter
import time
from tkinter import messagebox
from tkinter import Label

# canvas
canvasWidth = 300
canvasHeight = 300
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=canvasWidth, height=canvasHeight, bg="dodgerblue4")
canvas.pack()

bat = canvas.create_rectangle(0, 0, 40, 10, fill="dark turquoise")
ball = canvas.create_rectangle(0, 0, 10, 10, fill="deep pink")

windowOpen = True
global score
score = 0

# changes while playing
def main_loop():
    
    while windowOpen == True:
        move_bat()
        move_ball()
        window.update()
        time.sleep(0.02)
        if windowOpen == True:
            check_game_over()

# arrow keys
# 0 means not pressed
# 1 means pressed
leftPressed = 0
rightPressed = 0

# keys pressed
def on_key_press(event):
    global leftPressed, rightPressed
    if event.keysym == "Left":  # keysym links key to event
        leftPressed = 1
    elif event.keysym == "Right":
        rightPressed = 1

# keys released
def on_key_release(event):
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 0
    elif event.keysym == "Right":
        rightPressed = 0

# moving the bat
batSpeed = 6
def move_bat():
    batMove = batSpeed*rightPressed - batSpeed*leftPressed # 6 multiplied by the number of time you press an arrow key
    (batLeft, batTop, batRight, batBottom) = canvas.coords(bat)

    if (batLeft > 0 or batMove > 0) and (batRight < canvasWidth or batMove < 0):
        canvas.move(bat, batMove, 0)

# ball movement
ballMoveX = 4
ballMoveY = -4
setBatTop = -40
setBatTop = canvasHeight-40
setBatBottom = canvasHeight-30

# when ball hits the side
# when the ball hits the side, it moves the opposit direction
def move_ball():
    global score
    global ballMoveX, ballMoveY 
    (ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    # If  the ball hits the right edge
    if ballMoveX > 0 and ballRight > canvasWidth:
        ballMoveX = -ballMoveX
    # if the ball hits the left edge
    if ballMoveX < 0 and ballLeft < 0:
        ballMoveX = -ballMoveX
    # if the ball hits the top
    if ballMoveY < 0 and ballTop < 0:
        ballMoveY = -ballMoveY
    # if ball hits the bat
    if ballMoveY > 0 and ballBottom > setBatTop and ballBottom < setBatBottom:
        (batLeft, batTop, batRight, batBottom) = canvas.coords(bat)
        if ballRight > batLeft and ballLeft < batRight:
            ballMoveY = -ballMoveY
            
            # score            
            score += 1

            scoreLabel.config(text = "Score: " + str(score))

    canvas.move(ball, ballMoveX, ballMoveY)

# score label
scoreLabel = Label(window, text = "Score: " + str(score), bg="powder blue")
scoreLabel.place(x=5,y=5)

# if the ball goes past the bat
def check_game_over():

    (ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    if ballTop > canvasHeight:
        playAgain = tkinter.messagebox.askyesno(message="Do you want to play again?")

        if playAgain == True:
            reset()
        else:
            close()        

def close():
    global windowOpen
    windowOpen = False
    window.destroy()

# this resets the game if it is lost
def reset():
    global score
    global leftPressed, rightPressed
    global ballMoveX, ballMoveY
    leftPressed = 0
    rightPressed = 0
    ballMoveX = 4
    ballMoveY = -4
    # originall for bat = 10,  30
    canvas.coords(bat, 10, setBatTop, 30, setBatBottom)
    canvas.coords(ball, 20, setBatTop-10, 30, setBatTop)
    score = 0
    scoreLabel.config(text = "Score: " + str(score))

# keys
window.protocol("WM_DELETE_WINDOW", close)
window.bind("<KeyPress>", on_key_press)
window.bind("<KeyRelease>", on_key_release)

# call the functions
reset()
main_loop()

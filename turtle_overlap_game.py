#Turtle Game
import random
import turtle
screen=turtle.Screen()
screen.setup(100,100)
screen.bgcolor("cyan")
#function to check weather the turtle is in the screen return True/False
def isInScreen(win,turt):   
    leftBound = -win.window_width() / 2   
    rightBound = win.window_width() / 2   
    topBound = win.window_height() / 2   
    bottomBound = -win.window_height() / 2   
    turtleX = turt.xcor()  
    turtleY = turt.ycor()  
    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False   
    if turtleY > topBound or turtleY < bottomBound:
       stillIn = False  
    return stillIn
#Functionn to check if the turtle are in the same position returns True/False
def poscheck(x,y):
    same=False
    # xcor() and ycor() return the respective coordinates
    if x.xcor()==y.xcor() and x.ycor()==y.ycor(): 
        same=True
    return same
def main():
    wn = turtle.Screen()   
    june = turtle.Turtle()
    june.color("red")
    june.shape('turtle')
    july = turtle.Turtle()
    july.color("blue")
    july.shape('turtle')
    july.up()
    july.forward(50)
    july.down()

    while True:
        #calls the isInScrewen function to check if the turtle is in screen
        if isInScreen(wn,june):
            move=random.randint(1,3)
            #the turtle skips a chance if 3 is encountered randomly
            if move !=3:
                coin = random.randrange(0, 2)      
                if coin == 0:            
                    june.left(90)
                else:           
                    june.right(90)
                june.forward(50)
        else:
            june.write('blue turtle won')
            break
        #calls the isInScrewen function to check if the turtle is in screen
        if isInScreen(wn,july):
            move=random.randint(1,3)
            if move !=3:
                coin = random.randrange(0, 2)      
                if coin == 0:            
                    july.left(90)
                else:           
                    july.right(90)
                july.forward(50)
        else:
            july.write('red turtle won')
            break
        #call the poscheck function to see if the two turtles meet at the same position
        if poscheck(june,july)== True:
            july.write("there was no winner")
            break

    wn.exitonclick()
main()

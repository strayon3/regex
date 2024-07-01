import turtle
import random 


#spawn a number of turtles for drawing 
wm = turtle.Screen()
wm1 = turtle.screensize(3840, 2400)
colorOptions = ['#0048BA','#B0BF1A','#9F2B68','#FFBF00','9966CC'
                ,'#3DDC84','#C88A65','#665D1E','#915c83','#841B2D',
                '#00FFFF','#D0FF14','#4B6F44','#FF9966','#007FFF','#2E5894',
                '#CAE00D','#000000','#3D0C02','#54626F','#126180','#8A2BE2',
                '#5072A7','#004225','#7BB661','#00CC99','#00CC99']

jack = turtle.Turtle()



#itterate to get two cordinates the size of the screen 
for i in range(5):
    color1 = random.choice(colorOptions)
    currentHeight = random.randrange(-3840,3840)
    currentWidth = random.randrange(-2400,2400)
    jack.color(color1)
    jack.goto(currentHeight,currentWidth)
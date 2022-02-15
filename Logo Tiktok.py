from turtle import *

width(20)
bgcolor('#010101')
warna= ['#ee1d52', '#69c9d0', '#ffffff']
posisi= [(0,0), (-5,13), (-5,5)]

for (x,y),col in zip(posisi,warna):
    up()
    goto(x,y)
    down()
    color(col)
    left(180)
    circle(50, 270)
    forward(120)
    left(180)
    circle(50, 90)
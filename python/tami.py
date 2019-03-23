#!/usr/python
# coding=utf-8
# import turtle,os
# import time
# # turtle.pensize(2)
# turtle.bgcolor("black")
# colors = ["red","yellow",'purple','blue']
# turtle.tracer(False)
# for x in range(400):
# 	turtle.forward(2*x)
# 	turtle.color(colors[x%4])
# 	turtle.left(91)
# turtle.tracer(True)

from turtle import *
reset()
bgcolor('black')
speed(0)
colors = ['red','orange','green','cyan','blue','purple']
for i in range(360):
    pencolor(colors[i%6])
    fd(i*3/6+i)
    left(60)
    pensize(i*6/200)

# import turtle

# import time
# turtle.speed(2)

# # 设置初始位置  
# # 去到的坐标,窗口中心为0,0
# turtle.goto(0, 0)

# turtle.penup()  

# turtle.left(90)  

# turtle.fd(200)  

# turtle.pendown()  

# turtle.right(90)  

  

# # 花蕊  

# turtle.fillcolor("red")  

# turtle.begin_fill()  

# turtle.circle(10,180)  

# turtle.circle(25,110)  

# turtle.left(50)  

# turtle.circle(60,45)  

# turtle.circle(20,170)  

# turtle.right(24)  

# turtle.fd(30)  

# turtle.left(10)  

# turtle.circle(30,110)  

# turtle.fd(20)  

# turtle.left(40)  

# turtle.circle(90,70)  

# turtle.circle(30,150)  

# turtle.right(30)  

# turtle.fd(15)  

# turtle.circle(80,90)  

# turtle.left(15)  

# turtle.fd(45)  

# turtle.right(165)  

# turtle.fd(20)  

# turtle.left(155)  

# turtle.circle(150,80)  

# turtle.left(50)  

# turtle.circle(150,90)  

# turtle.end_fill()  

   

# # 花瓣1  

# turtle.left(150)  

# turtle.circle(-90,70)  

# turtle.left(20)  

# turtle.circle(75,105)  

# turtle.setheading(60)  

# turtle.circle(80,98)  

# turtle.circle(-90,40)  

  

# # 花瓣2  

# turtle.left(180)  

# turtle.circle(90,40)  

# turtle.circle(-80,98)  

# turtle.setheading(-83)  

  

# # 叶子1  

# turtle.fd(30)  

# turtle.left(90)  

# turtle.fd(25)  

# turtle.left(45)  

# turtle.fillcolor("green")  

# turtle.begin_fill()  

# turtle.circle(-80,90)  

# turtle.right(90)  

# turtle.circle(-80,90)  

# turtle.end_fill()  

   

# turtle.right(135)  

# turtle.fd(60)  

# turtle.left(180)  

# turtle.fd(85)  

# turtle.left(90)  

# turtle.fd(80)  

   

# # 叶子2  

# turtle.right(90)  

# turtle.right(45)  

# turtle.fillcolor("green")  

# turtle.begin_fill()  

# turtle.circle(80,90)  

# turtle.left(90)  

# turtle.circle(80,90)  

# turtle.end_fill()  

   

# turtle.left(135)  

# turtle.fd(60)  

# turtle.left(180)  

# turtle.fd(60)  

# turtle.right(90)  

# turtle.circle(200,60)  
# time.sleep(2)
# turtle.clear()
# turtle.reset()

# # 画爱心的顶部
# def LittleHeart():
#     for i in range(200):
#         turtle.right(1)
#         turtle.forward(2)



# # 输入署名或者赠谁，没有不执行
# me = 'code by Lang'
# love = 'I Love Tami'
    
# # 窗口大小
# # turtle.setup(width=1000, height=500)
# # 颜色
# turtle.color('red', 'pink')
# # 笔粗细
# turtle.pensize(3)
# # 速度
# turtle.speed(1)
# turtle.right(0)
# # 提笔
# turtle.up()
# # 隐藏笔
# turtle.hideturtle()
# # 去到的坐标,窗口中心为0,0
# turtle.goto(0, -180)
# turtle.showturtle()
# # 画上线
# turtle.down()
# turtle.speed(1)
# turtle.begin_fill()
# turtle.left(140)
# turtle.forward(224)
# # 调用画爱心左边的顶部
# LittleHeart()
# # 调用画爱右边的顶部
# turtle.left(120)
# LittleHeart()
# # 画下线
# turtle.forward(224)
# turtle.end_fill()
# turtle.pensize(5)
# turtle.up()
# turtle.hideturtle()
# # 在心中写字 一次
# turtle.goto(0, 0)
# turtle.showturtle()
# turtle.color('#CD5C5C', 'pink')
# # 在心中写字 font可以设置字体自己电脑有的都可以设 align开始写字的位置
# turtle.write(love, font=('gungsuh', 30,), align="center")
# turtle.up()
# turtle.hideturtle()
# time.sleep(1)
# # 在心中写字 二次
# turtle.goto(0, 0)
# turtle.showturtle()
# turtle.color('red', 'pink')
# turtle.write(love, font=('gungsuh', 30,), align="center")
# turtle.up()
# turtle.hideturtle()
# # 写署名
# if me != '':
#     turtle.color('black', 'pink')
#     time.sleep(2)
#     turtle.goto(180, -180)
#     turtle.showturtle()
#     turtle.write(me, font=(20,), align="center", move=True)

# 点击窗口关闭
window = Screen()
window.exitonclick()
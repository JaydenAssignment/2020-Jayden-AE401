#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:46:53 2020

@author: jaydenjian
"""

#召喚模組
import turtle

#創造一個畫布
C=turtle.Screen()
#設定畫布視窗名稱
C.title("my window")
#設定背景顏色
C.bgcolor("black")

#生成烏龜
a=turtle.Turtle()

#設定烏龜(畫筆)樣式
a.color("yellow")
a.shape("turtle")

j=0.1 
#加入for迴圈
for i in range(720):   
    #移動烏龜
    a.right(1)
    a.forward(j)
    j=j+0.005 #j要加多少可以慢慢測試
    i=i+1
        
#結束烏龜畫畫    
turtle.done()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:47:54 2020

@author: jaydenjian
"""
#匯入模組
import random

#產生一個隨機的數字
num = random.randint(1,10)

#輸入
a=input("請輸入數字：")
#強制轉型
a=int(a)

while True:
    #判斷
    if a==num:
        print("恭喜你猜對了！")
        break
    else: 
        a=input("再猜一次數字：")
        a=int(a)

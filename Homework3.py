#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:02:01 2020

@author: jaydenjian
"""
#召喚模組
import random
#隨機生成1~20一個數字
ans=random.randint(1,20)

#輸入
num=input("5次機會，請輸入1~20其中一數字：")
#強制轉型
num=int(num)

i=0 #次數
while i < 5:
    #判斷
    if num>0 and num<=20:
        
        if num==ans:
            i=i+1
            print("恭喜你猜對了！")
            break
        
        elif num<ans:
            i=i+1
            print("比答案小喔!")
            num=input("猜錯了，請再猜一個數字：")
            #再強制轉型一次
            num=int(num)
        else: #num>ans
            i=i+1
            print("比答案大喔!")
            num=input("猜錯了，請再猜一個數字：")
            #再強制轉型一次
            num=int(num)
    else:
        print("輸入錯誤！")
        
print("遊戲結束～你總共猜了：",i,"次","答案是：",ans)
        


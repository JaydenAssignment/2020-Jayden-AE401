#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:07:52 2020

@author: jaydenjian
"""
#先建立一個空的數學成績清單
math=list()

#詢問人數
num=int(input("全班人數："))


#將姓名、成績放入「成績清單」
for i in range(num):
    name=input("學生姓名：")
    score=int(input("數學成績："))
    
    
    student=list()  #再放入清單之前先建立一個學生的「個人小清單」
    
    student.append(name)  #將名字、成績，放入學生個人清單
    student.append(score)
    
    math.append(student) #將「個人清單」放入「數學成績清單」

#顯示數學成績清單
print("數學成績單 :",math)   
#################################################

#計算平均成績
Sum=0

for i in range(num):      
    Sum=Sum+math[i][1] 
    
#平均
Avg=Sum/num
print("平均成績 =", Avg)
#################################################

#計算最高分
highest=0

for i in range(num):
    if math[i][1]>highest:
        highest=math[i][1]
        #要將最高分的人的名字先記下來
        highestStudent=math[i][0]

print("最高分是",highestStudent, highest,"分")
#################################################

#計算最低分

lowest=100

for i in range(num):
    if math[i][1]<lowest:
        lowest=math[i][1]
        #要將最低分的人的名字先記下來
        lowestStudent=math[i][0]

print("最低分是",lowestStudent, lowest,"分")











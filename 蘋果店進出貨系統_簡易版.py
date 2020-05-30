#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:15:28 2020

@author: jaydenjian
"""
while True:
    print("-------蘋果店交易系統-------")
    print("  1.設定庫存數量、單價")
    print("  2.進貨")
    print("  3.出貨/交易")
    print("  4.離開系統")
      
    function=int(input("請輸入欲使用功能選項："))
    
    print("-------------------------")
    
    
    if function==1:
        ##### 功能一 #####
        myApple=int(input("現有庫存蘋果："))
        applePrice=int(input("單價："))
        print("目前庫存：",myApple,"顆 蘋果")
        print("一顆蘋果",applePrice,"元")
    elif function==2:
        ##### 功能二 #####
        appleIn=int(input("進貨蘋果數量："))
        myApple = myApple + appleIn
        print("進貨了",appleIn,"顆")
        print("目前庫存：",myApple,"顆")
    elif function==3:
        ##### 功能三 #####
        appleOut=int(input("交易蘋果數量："))
        total=appleOut * applePrice
        myApple = myApple - appleOut
        print("應收金額：",total,"元")
        print("目前庫存：",myApple,"顆")
    elif function==4:
        ####功能四#######
        print("感謝使用本系統！")
        break
    

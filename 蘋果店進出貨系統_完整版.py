#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:52:25 2020

@author: jaydenjian
"""

sellRecord=[] #設定空的交易紀錄清單(帳單)

while True:
    print("-------蘋果店交易系統-------")
    print("  1.設定庫存數量、單價")
    print("  2.進貨")
    print("  3.出貨/交易")
    print("  4.營業額統計")
    print("  5.庫存統計")
    print("  6.離開系統")
      
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
        
        sellRecord.append(appleOut) #將此次交易記錄到清單中
        
    elif function==4:
        total=0 #總收入初始值
        print("\n目前交易紀錄：")
        for i in range(len(sellRecord)): #利用len()計算清單長度，讓迴圈依據清單長度跑幾次
                #印出第幾筆資料 / 賣出幾顆  /  售出多少元
            print(i+1,".賣出",sellRecord[i],"顆", sellRecord[i] * applePrice,"元")
            total=total+(sellRecord[i] * applePrice)
            
        print("總收入：", total,"元")
            
    elif function==5: 
        print("目前庫存：",myApple,"顆")
        
    elif function==6:
        ####功能四#######
        print("感謝使用本系統！")
        break
    else:
        #如果輸入的功能不是數字1~4，就印出「請輸入功能數字1~4！」
        print("請輸入功能數字1~4！")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:18:18 2020

@author: jaydenjian
"""

#建立一個空的字典
d={}

while True:    
    key=input("請輸入單字(按0跳出)：") #請使用者輸入單字
    
    #當輸入為0時，跳出程式
    if key == str(0):    #鍵盤輸入的是字串，所以判斷用的0也要當字串
        print(d)        #可以用 str(0)也可以直接 "0"
        break
    else:
        #如果輸入沒有在原本字典裡的話,就存進字典裡
        if key not in d.keys():
            value=input("請輸入翻譯：")
            d[key]=value
        else: #如果原本就在字典裡,就不用輸入中文
            print("此單字已在字典中，請輸入其他單字！")
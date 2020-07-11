#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 10:41:09 2020

@author: jaydenjian
"""
import os.path

content="" #清除之前記憶

while True:
    print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
    print("歡迎使用字串處理器")
    print("---------------------")
    print("功能：")
    print("1. 輸入檔案")
    print("2. 單字統計表")
    print("3. 查詢檔案中單字")
    print("4. 替換檔案中單字")
    print("5. 離開系統")
    print("---------------------")
    function=input("請輸入要使用的功能選項：")
    print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")

    ### 功能一 ##########################    
    if function=="1":        
        fileName=input("請輸入檔名(含副檔名):")        
        if os.path.isfile(fileName):            
            file=open(fileName,"r") #打開文件,讀取模式
            content=file.read()     #讀取文件內容
            print("\n",content)
            
        else:            
            print("沒有此文件！") 
            
        file.close()
    ### 功能二 ##########################
    elif function=="2":          
        if content:
            wordList=content.split()
            print("文件共有",len(wordList),"個字")
        else:
            print("沒有內容！請先輸入檔案！")
     
    ### 功能三 ##########################     
    elif function=="3":            
        wordCount=0
        noThisWord=False
        if content:
            searchWord=input("請輸入要搜尋的單字：")
            wordCount=content.count(searchWord)
            #################### 確定是單字而不是單純的字母 ####################
            wordList=content.split() #分割字串           
            for i in range(len(wordList)): #檢查字串中的每個單詞是否有輸入的單字(用字串的長度len跑迴圈)
                if searchWord==wordList[i]: #在字串中有此單字(字母不算單字)
                    print(searchWord,"共出現了",wordCount,"次") #印出共有幾次(前面已經有數過了)
                    noThisWord=False #一個字一個字檢查，有就false，沒有就true
                    break #有這個單詞的話就直接跳出for迴圈
                else:
                    noThisWord=True 
                    
            if noThisWord:
                print("沒有出現此單字！")
            ###############################################################
        else:
            print("沒有內容！請先輸入檔案！")
            
    ### 功能四 ##########################            
    elif function=="4":                 
        if content:
            oldWord=input("請輸入要替換的單字：")
            newWord=input("請輸入新的單字：")
            content=content.replace(oldWord,newWord)
            print("更新後內容：\n", content)
            file=open(fileName,"w") #打開文件,寫入模式
            file.write(content) #更新寫入新字串
            file.close()
        else:
            print("沒有內容！請先輸入檔案！")
            
    ### 功能五 ##########################              
    elif function=="5":
        print("離開系統...")
        break
    
    else:
        print("輸入錯誤！請重新輸入！")
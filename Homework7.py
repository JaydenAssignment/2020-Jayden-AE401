#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:37:41 2020

@author: jaydenjian
"""
#匯入函式庫(召喚)
import random

#設定名字、動詞、名詞 清單
nameList=["John", "Amy", "Andy"]
verbList=["正在踢", "正在打", "正在玩"]
nounList=["足球","球","皮球"]

#定義自己的函式
def random_word(list):  #從每個清單中抓出一個元素(一個字詞)
    
    #random.sample(x,1)會回傳一個list
    #例如：random.sample(nameList,1)，他會回傳["John"]或["Amy"]或["Andy"]
    #但我們要的是字串(str)就好，所以取得清單中第一個元素的方法就是list[0]
    #因此這裡才在後面加了一個[0]
    word=random.sample(list,1)[0]
    
    return word
    
#產生句子
def generateSentence(list1,list2,list3):
    
    #在這個函式中，呼叫前面自己定義的函式
    #各從三個清單中隨機取得一個元素，並把它加起來，形成一個句子
    sentence = random_word(list1) + random_word(list2) + random_word(list3)
    
    return sentence #回傳這個句子

for i in range(5):
    #直接在print中呼叫自定義的函式，並印出
    print(generateSentence(nameList, verbList, nounList))
    

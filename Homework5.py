#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:05:11 2020

@author: jaydenjian
"""

scores=[]

for i in range(5):
    a=input("請輸入分數：")
    #強制轉型
    a=int(a)
    scores.append(a)

print(scores)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 12:09:50 2020

@author: jaydenjian
"""

score=input("請輸入成績：")

score=int(score)

if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70  :
    print("C")  
else:
    print("D")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:08:28 2020

@author: jaydenjian
"""

math=input("請輸入數學成績：")
eng=input("請輸入英文成績：")
math=int(math)
eng=int(eng)

if math>=90 and eng>=90:
    print("有獎品！")
elif math<60 and eng<60:
    print("要懲罰！")
elif math<=60 or eng<=60:
    print("再加油！")
else:
    print("pass!")
    
    
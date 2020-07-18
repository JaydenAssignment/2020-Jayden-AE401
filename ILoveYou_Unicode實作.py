#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 11:04:04 2020

@author: jaydenjian
"""
chars=[]

myString="I Love YOU"
for c in myString:
    chars.append(ord(c))
    print(c,"的unicode是：",ord(c))

    
##########################

print("將所有unicode+2後，轉成文字是：", end = '')

for num in chars:
    print(chr(num+2),end = '')

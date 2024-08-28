# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:55:15 2024

@author: Admin
"""



a=int(input("nhập số a:"))
b=int(input("nhập số b:"))
c=int(input("nhập số c:"))
d=int(input("nhập số d:"))

if a<b and a<c and a<d:
    print(" a là số nhỏ nhất:")
elif b<a and b<c and b<d:
    print("b là số nhỏ nhất")
elif c<a and c<b and c<d:
    print(" c là số nhỏ nhất")
elif d<a and d<b and d<c:
    print(" d là số nhỏ nhất")

    
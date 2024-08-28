# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:38:58 2024

@author: Admin
"""

a=float(input(" nhập a:"))
b=float(input(" nhập b:"))
if a==0 and b==0:
    print("phương trình vô số nghiệm")
if a==0 and b!=0:
    print("phương trình vô nghiệm")
if a!=0:
    x= -b/a
    print(f"phương trình có nghiệm duy nhất: x={x}")
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:18:38 2024

@author: Admin
"""

a=input("nhập chữ cái bất kỳ:")
# chữ thường thành chữ hoa
if a.islower():
 a=a.upper()
 print("Chữ tương ứng là:", a)
#hoa thành thường
elif a.isupper():
 a=a.lower()
 print("Chữ tương ứng là:",a)
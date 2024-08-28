# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:10:27 2024

@author: Admin
"""

h=int(input("nhập giờ:"))
p=int(input("nhập phút:"))
s=int(input("nhập giây:"))
if 0<= h <=24:
    print("Giờ hợp lệ")
else:
        print("Giờ không hợp lệ")
if 0<= p <=60:
    print("Phút hợp lệ")
else:
    print("Phút hợp lệ")
if s>=0:
    print("Giây hợp lệ")
else:
    print("Giây không hợp lệ")
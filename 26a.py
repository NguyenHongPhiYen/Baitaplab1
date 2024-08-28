# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:38:39 2024

@author: Admin
"""

a=float(input("nhập a:"))
b=float(input("nhập b:"))
c=float(input("nhập c:"))
if a>b:
    a, b = b, a

if a > c:
    # Đổi chỗ a và c
    a, c = c, a

if b > c:
    # Đổi chỗ b và c
    b, c = c, b

print("Thứ tự tăng dần của ba số là:", a, b, c)
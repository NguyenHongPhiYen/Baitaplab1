# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:56:35 2024

@author: Admin
"""

a=int(input("nhập số nguyên đầu tiên:"))
b=int(input("nhập số nguyên thứ hai:"))
c=int(input("nhập số nguyên thứ ba:"))
d=int(input("nhập số nguyên thứ tư:"))
if a>b:
    a, b = b, a

if a > c:
    # Đổi chỗ a và c
    a, c = c, a
if a>d:
    a,d=d,a
if b > c:
    # Đổi chỗ b và c
    b, c = c, b
if b > d:
    b, d = d, b

if c > d:
    c, d = d, c
print("Theo thứ tự tăng dần là", a,b,c,d)

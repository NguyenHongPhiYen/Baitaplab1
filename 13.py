# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:52:04 2024

@author: Admin
"""

a=int(input("nhập ngày sinh:"))
b=int(input("nhập tháng sinh:"))
c=int(input("nhập năm sinh:"))
#trường hợp a
cau_a= f"{a}/{b}/{c}"
print(cau_a)

#trường hợp b
cau_b= f"{a}/{b}/{c%100}"
print(cau_b)

#trường hợp c
cau_c= f"{c}/{b}/{a}"
print(cau_c)
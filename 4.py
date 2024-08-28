# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 22:33:00 2024

@author: Admin
"""

import math
N=int(input("Nhập số nguyên dương N có 2 chữ số:"))
if 10<= N <= 99:
 Tong=(N//10)+(N%10)
print("Tổng của 2 chữ số của N:", Tong)
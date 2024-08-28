# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:04:46 2024

@author: Admin
"""

import math
#khung giờ thứ nhất
h1=int(input("nhập giờ thứ nhất:"))
p1=int(input("nhập phút thứ nhất:"))
s1=int(input("nhập giờ thứ nhất:"))
T1= h1*3600 + p1*60 +s1
#khung giờ thứ hai
h2=int(input("nhập giờ thứ hai:"))
p2=int(input("nhập phút thứ hai:"))
s2=int(input("nhập giây thứ hai:"))
T2= h2*3600 + p2*60 +s2
Cong= T1 + T2
Tru= T1 - T2
print("Tổng thời gian 2 khung giờ qua giây là:", Cong)
print("Hiệu thời gian 2 khung giờ qua giây là", Tru)
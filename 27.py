# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:03:43 2024

@author: Admin
"""

#import math
hinh=input("chọn hình:")
#hình vuông
if hinh == 'v':
 v=input("hình vuông")
 chieu_dai=float(input("nhập chiều dài cạnh hình vuông:"))
 chu_vi_v= chieu_dai*4
 dien_tich_v= chieu_dai**2
 print("Chu vi hình vuông là", chu_vi_v)
 print("Diện tích hình vuông là", dien_tich_v)  
#hình chữ nhật  
elif hinh== 'n':
 n=input("hình chữ nhật")
 dai=float(input("nhập chiều dài hình chữ nhật:"))
 rong=float(input("nhập chiều rộng hình chữ nhật:"))
 chu_vi_n= (dai+rong)*2
 dien_tich_n= dai*rong
 print("Chu vi hình chữ nhật là", chu_vi_n)
 print("Diện tích hình chữ nhật là", dien_tich_n)
#hình tròn
elif hinh== 't':
 t=input("hình tròn")
 R=float(input("nhập số đo bán kính:"))
 chu_vi_t= R*2*3.14
 dien_tich_t= R*R*3.14
 print("Chu vi hình tròn là", chu_vi_t)
 print("Diện tích hình tròn là", dien_tich_t)
 
 
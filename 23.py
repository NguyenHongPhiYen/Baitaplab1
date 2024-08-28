# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:48:33 2024

@author: Admin
"""

a=float(input("nhập a:"))
b=float(input("nhập b:"))
c=float(input("nhập c:"))
if a==0 and b==0 and c==0:
    print("phương trình vô số nghiệm")
if a==0:
    print("phương trình bậc nhất")

delta= b**2 - 4*a*c
if delta >0:
 x1=( -b + ( (delta)**(1/2)) / 2*a )
 x2=( -b - ( (delta)**(1/2)) / 2*a )
 print(f"phương trình có 2 nghiệm là: x1={x1}, x2={x2}")
elif delta ==0:
 x= -b/(2*a)
 print(f"phương trình có nghiệm kép là: x1 = x2 ={x}")
elif delta < 0:
    print("phương trình vô nghiệm")
 

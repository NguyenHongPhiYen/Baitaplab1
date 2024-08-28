# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:14:14 2024

@author: Admin
"""

import math
a=float(input("nhập a:"))
b=float(input("nhập b:"))
A=( (a+b)/ ( (a**(1/3)) + (b**(1/3)) )) - ( (a*b)**(1/3))
B=(( (a**(1/3)) - (b**(1/3)))**2)
print(A/B)
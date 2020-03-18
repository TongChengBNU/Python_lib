# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 13:55:45 2020

@author: 75934
"""

import time
scale = 50
print("Start".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
    time.sleep(0.1)
print("\n" + "End".center(scale//2, "-"))

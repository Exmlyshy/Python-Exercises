#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-06 09:29:08
import time

c={0:0,1:1,2:1,3:2}
i=0

def fib(n):
    global c
    global i
    i+=1
    if n not in c:
        if n%2==0:
            c[n]=fib(n//2)*(fib(n//2+1)+fib(n//2-1))
        else:
            c[n]=fib(n//2)*fib(n//2)+fib(n//2+1)*fib(n//2+1)
    return c[n]

t=time.time()
r=fib(1000000)
print(time.time()-t)
print(len(str(r)))
print(i)

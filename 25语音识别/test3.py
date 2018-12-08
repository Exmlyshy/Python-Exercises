#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-02 19:42:33
import time

                                                                         
# print("Loading",end = "")
# # for i in range(6):
# #     print(".",end = '')
# #     time.sleep(0.2)
i=0
while True:
    print('\r'+str(i),end='')
    i+=1
    time.sleep(0.3)

# while True:
#     print('\rLoading',end='')
#     for i in range(1,7):
#         # print('\r'+'.'*i+' '*(6-i),end='')
#         print('.',end='',flush=True)
#         time.sleep(0.3)
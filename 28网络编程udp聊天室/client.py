#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-22 19:52:23
import socket
import time
import threading 


def recv(sock:socket.socket,addr): 
    '''
    一个UDP连接在接收消息前必须要让系统知道所占端口
    也就是需要send一次，否则会win下报错
    “   data=sock.recv(1024)
        OSError: [WinError 10022] 提供了一个无效的参数。   ”
    '''
    sock.sendto(name.encode('utf-8'),addr)
    while True:
        data=sock.recv(1024)
        print(data.decode('utf-8'))



def send(sock,addr):
    while True:
        string=name+':'+input()
        data=string.encode('utf-8')
        sock.sendto(data,addr)
        if 'EXIT' in string:
            break
    



def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server=('127.0.0.1',9999)


    tr=threading.Thread(target=recv,args=(s,server),daemon=True)
    ts=threading.Thread(target=send,args=(s,server))
    tr.start()
    ts.start()
    

if __name__ == '__main__':
    print("欢迎来到聊天室,退出聊天室请输入'EXIT'")
    name=input('你的名字:')
    main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-21 14:32:52
import time
import queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


def main():
    QueueManager.register('get_s2c_queue')
    QueueManager.register('get_c2s_queue')

    server_addr='127.0.0.1'
    print('Connect to server %s...'%server_addr)

    m=QueueManager(address=(server_addr,5000),authkey=b'hello')
    m.connect()

    s2c=m.get_s2c_queue()
    c2s=m.get_c2s_queue()

    while True:
        try:
            message_from=s2c.get(timeout=60)
            print('Reply:%s'%message_from)
            message_to=input('You:')
            c2s.put(message_to)
        except queue.Empty:
            print('No reply.')
        except ConnectionResetError:
            print('Server has just shutdown.')
            break

if __name__ == '__main__':
    main()
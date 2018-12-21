#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-21 11:06:27
import time
import queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass

s2c_queue = queue.Queue()
c2s_queue = queue.Queue()


def get_s2c():
    return s2c_queue


def get_c2s():
    return c2s_queue


def main():
    QueueManager.register('get_s2c_queue', callable=get_s2c)
    QueueManager.register('get_c2s_queue', callable=get_c2s)

    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'hello')

    manager.start()

    s2c = manager.get_s2c_queue()
    c2s = manager.get_c2s_queue()

    print('start to chat,input "EXIT" to exit...')
    while True:
        try:
            message_to = input('You:')
            if message_to == 'EXIT':
                manager.shutdown()
                print('shutdown.')
                break
            s2c.put(message_to)
            message_from = c2s.get(timeout=60)
            print('Reply:%s' % message_from)
        except queue.Empty:
            print('No reply.')


if __name__ == '__main__':
    main()

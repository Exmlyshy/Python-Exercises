#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-22 18:46:00
import socket
import time
import threading
import logging
logging.basicConfig(level=logging.INFO)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    addr = ('127.0.0.1', 9999)
    s.bind(addr)

    logging.info('UDP Server on %s:%s...', addr[0], addr[1])

    user = {}  # {addr:name}
    while True:
        try:
            data, addr = s.recvfrom(1024)
            if not addr in user:
                for address in user:
                    s.sendto(data + ' 进入聊天室...'.encode(), address)
                user[addr] = data.decode('utf-8')
                continue

            if 'EXIT' in data.decode('utf-8'):
                name = user[addr]
                user.pop(addr)
                for address in user:
                    s.sendto((name + ' 离开了聊天室...').encode(), address)
            else:
                print('"%s" from %s:%s' %
                      (data.decode('utf-8'), addr[0], addr[1]))
                for address in user:
                    if address != addr:
                        s.sendto(data, address)

        except ConnectionResetError:
            logging.warning('Someone left unexcept.')


if __name__ == '__main__':
    main()

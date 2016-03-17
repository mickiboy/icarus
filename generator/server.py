#!/bin/env python3
#
# icarus cms
#
# (c) 2016 Daniel Jankowski

import socket

from threading import Thread, Event

import util

from util import *

class management_server(Thread):

    def __init__(self, port, addr):
        super().__init__()
        self.stop_event = Event()
        self.port = port
        self.addr = addr
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__connections = []

    def __shutdown(self):
        for c in self.__connections:
            c.stop_event.set()

    def run(self):
        # bind socket
        self.socket.bind((self.addr, self.port))
        self.socket.listen(2)
        self.socket.settimeout(1.0)

        # wait for incoming connections
        while not self.stop_event.is_set():
            try:
                conn = self.socket.accept()
            except socket.timeout:
                continue
            
            # append connections to open connections
            tct = tcp_connection_thread(conn[0], conn[1])
            self.__connections.append(tct)
            tct.set_callback(self)
            
            # start connection thread
            tct.start()
            self.stop_event.wait(1.0)
        self.__shutdown()


class tcp_connection_thread(Thread):

    def __init__(self, socket, peer):
        super().__init__()
        self.stop_event = Event()
        self.__socket = socket
        self.__peer = peer
        self.__callback = None

    def __shutdown(self):
        self.__socket.close()
        self.__socket = None

    def set_callback(self, callback):
        self.__callback = callback

    def run(self):
        while not self.stop_event.is_set():
            # wait for incoming data
            try:
                data = self.__socket.recv(4096)
            except socket.timeout:
                continue
        self.__shutdown()


def main():
    print('module tests\n')
    
    log('management server thread')
    try:
        ms = management_server(4567, '127.0.0.1')
    except Exception as e:
        log_err('while starting the management server thread')
        print(str(e))
        return
    log('closing management server thread')
    try:
        ms.stop_event.set()
    except Exception as e:
        log_err('while stopping the management server thread')
        print(str(e))
        return
    log('Success!')
    pass


if __name__ == '__main__':
    main()

import socket
import time
import threading
from .jfAPI import (
    screenshot,
)
from typing import Optional

class ScreenServer:
    def __init__(
        self, 
        addr: tuple[str, int] = ('127.0.0.1', 27013),
        listenumber: int = 1,
        screensize: int = (1080, 720),
        prick_addr: Optional[tuple[str, int]] = None,
        ) -> None:
        self.host, self.port = addr
        self.listenumber = listenumber
        self.screensize = screensize
        self.isprick = False        
        if prick_addr != None:
            self.prick_host, self.prick_port = prick_addr
            self.isprick = True

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __screenshot_send(self, sk: socket.socket):
        while True:
            time.sleep(1)
            frame = screenshot(self.screensize)
            sk.send(frame)
            print('send len' + str(len(frame)))

    def run_normal(self):
        self.__socket.bind((self.host, self.port))
        self.__socket.listen(self.listenumber)

        print('screen等待客户端链接...')
        sk, addr = self.__socket.accept()
        print(f"客户端: {addr} 链接...")

        threading.Thread(target = self.__screenshot_send, args=(sk, ), name = 'screenshot_send').start()

    def run_prick(self):
        self.__socket.connect((self.prick_host, self.prick_port))
        print('screenshot已成功链接, 等待命令...')
        self.__socket.send('send'.encode('utf-8'))
        data = self.__socket.recv(1024).decode('utf-8')
        if data == 'ok':
            threading.Thread(target = self.__screenshot_send, args=(self.__socket, ), name = 'screenshot_send').start()
        print('screenshot开始运行...')

    
    def run(self):
        if self.isprick == True:
            self.run_prick()
        else:
            self.run_normal()
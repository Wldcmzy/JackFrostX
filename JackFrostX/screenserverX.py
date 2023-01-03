import socket
import time
import threading
from .eventAPI import (
    screenshot,
)

class ScreenServer:
    def __init__(
        self, 
        addr: tuple[str, int] = ('127.0.0.1', 27013),
        listenumber: int = 1,
        screensize: int = (1080, 720),
        ) -> None:
        self.host, self.port = addr
        self.listenumber = listenumber
        self.screensize = screensize

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __screenshot_send(self, sk: socket.socket):
        while True:
            time.sleep(1/20)
            frame = screenshot(self.screensize)
            sk.send(frame)

    def run(self):
        self.__socket.bind((self.host, self.port))
        self.__socket.listen(self.listenumber)

        print('等待客户端链接...')
        sk, addr = self.__socket.accept()
        print(f"客户端: {addr} 链接...")

        threading.Thread(target = self.__screenshot_send, args=(sk, ), name = 'screenshot_send').start()

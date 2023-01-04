import socket
import pyautogui
import threading
from typing import Optional

class KeyboardServer:
    def __init__(
        self, 
        addr: tuple[str, int] = ('127.0.0.1', 27014),
        buffersize: int = 1024,
        listenumber: int = 1,
        prick_addr: Optional[tuple[str, int]] = None
        ) -> None:
        self.host, self.port = addr
        self.listenumber = listenumber
        self.buffersize = buffersize
        self.isprick = False
        if prick_addr != None:
            self.prick_host, self.prick_port = prick_addr
            self.isprick = True
            

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __keyboard_receive(self, sk: socket.socket):
        while True:
            data = sk.recv(self.buffersize).decode('utf-8')
            try:
                lst = data[ : -1].split('#')
                for each in lst:
                    mode, key = each.split(':')
                    if mode == 'up':
                        pyautogui.keyUp(key)
                    else:
                        pyautogui.keyDown(key)
            except:
                print(data)

    def run_normal(self):
        self.__socket.bind((self.host, self.port))
        self.__socket.listen(self.listenumber)

        print('keyboard等待客户端链接...')
        sk, addr = self.__socket.accept()
        print(f"客户端: {addr} 链接...")

        threading.Thread(target = self.__keyboard_receive, args=(sk, ), name = 'screenshot_send').start()

    def run_prick(self):
        self.__socket.connect((self.prick_host, self.prick_port))
        print('keyboard已成功链接, 等待命令...')
        self.__socket.send('receive'.encode('utf-8'))
        data = self.__socket.recv(self.buffersize).decode('utf-8')
        if data == 'ok':
            threading.Thread(target = self.__keyboard_receive, args=(self.__socket, ), name = 'screenshot_send').start()
        print('keyboard开始运行...')

    def run(self):
        if self.isprick == True:
            self.run_prick()
        else:
            self.run_normal()
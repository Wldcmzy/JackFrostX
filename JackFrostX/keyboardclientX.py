import socket
import keyboard
import threading
from typing import Optional

class KeyboardClient:
    def __init__(
        self, 
        addr: tuple[str, int] = ('127.0.0.1', 27014),
        buffersize: int = 1024,
        prick_addr: Optional[tuple[str, int]] = None
        ) -> None:
        self.host, self.port = addr
        self.buffersize = buffersize
        self.isprick = False
        if prick_addr != None:
            self.prick_host, self.prick_port = prick_addr
            self.isprick = True

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__keyboard = {
            'w' : 'up',
            'a' : 'up',
            's' : 'up',
            'd' : 'up',
        }

    def __callback(self, x):
        mode, key = x.event_type, x.name
        if key in self.__keyboard:
            if self.__keyboard[key] != mode:
                self.__keyboard[key] = mode
                self.__socket.send(f'{mode}:{key}#'.encode('utf-8'))

    def __listening(self):
        keyboard.hook(self.__callback)
        keyboard.wait()
    
    def run_normal(self):
        self.__socket.connect((self.host, self.port))
        threading.Thread(target = self.__listening, name = 'keyboard_listen_and_send').start()

    def run_prick(self):
        self.__socket.connect((self.prick_host, self.prick_port))
        print('keyboard已成功链接, 等待命令...')
        self.__socket.send('send'.encode('utf-8'))
        data = self.__socket.recv(self.buffersize).decode('utf-8')
        if data == 'ok':
            threading.Thread(target = self.__listening, name = 'keyboard_listen_and_send').start()
        print('keyboard开始运行...')

    def run(self):
        if self.isprick == True:
            self.run_prick()
        else:
            self.run_normal()
        
        

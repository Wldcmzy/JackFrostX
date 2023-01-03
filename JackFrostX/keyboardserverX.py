import socket
import pyautogui
import threading

class KeyboardServer:
    def __init__(
        self, 
        addr: tuple[str, int] = ('127.0.0.1', 27014),
        buffersize: int = 1024,
        listenumber: int = 1,
        ) -> None:
        self.host, self.port = addr
        self.listenumber = listenumber
        self.buffersize = buffersize

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

    def run(self):
        self.__socket.bind((self.host, self.port))
        self.__socket.listen(self.listenumber)

        print('等待客户端链接...')
        sk, addr = self.__socket.accept()
        print(f"客户端: {addr} 链接...")

        threading.Thread(target = self.__keyboard_receive, args=(sk, ), name = 'screenshot_send').start()

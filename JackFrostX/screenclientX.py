import socket
import threading
from tkinter import *
from io import BytesIO
from PIL import ImageTk, Image
from typing import Optional

class ScreenClient:
    def __init__(
        self, 
        addr: tuple[str, int] = ('127.0.0.1', 27013),
        buffersize: int = 2**20,
        screensize: tuple[int, int] = (1440, 810),
        prick_addr: Optional[tuple[str, int]] = None,
        ) -> None:

        self.__root = Tk()
        self.__root.resizable(0, 0)
        self.__root.title('JackFrostX')
        self.__lebel = Label(self.__root, image = None)
        self.screensize = screensize
        self.temp = None
        self.isprick = False
        if prick_addr != None:
            self.prick_host, self.prick_port = prick_addr
            self.isprick = True

        self.host, self.port = addr
        self.buffersize = buffersize
        self.__pool = []

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        
        

    def __screenshot_receive(self):
        while True:
            data = self.__socket.recv(self.buffersize)
            self.__pool.append(data)
    
    def __play(self):
        self.__lebel.pack()
        counter = 0
        while True:
            if len(self.__pool) > 0:
                print('lenpool = ' + str(len(self.__pool)))
                frame = self.__pool.pop(0)
                print('framelen = ' + str(len(frame)))
                try:
                    img = ImageTk.PhotoImage(Image.open(BytesIO(frame)).resize(self.screensize))
                    self.__lebel.configure(image=img)
                    self.temp = img
                except:
                    counter += 1
                    print('err >>> ' + str(counter))
    
    def run_normal(self):
        self.__socket.connect((self.host, self.port))
        threading.Thread(target = self.__play, name = 'playX').start()
        threading.Thread(target = self.__screenshot_receive, name = 'screenshot_receiveX').start()
        self.__root.mainloop()

    def run_prick(self):
        self.__socket.connect((self.prick_host, self.prick_port))
        print('screen已成功链接, 等待命令...')
        self.__socket.send('receive'.encode('utf-8'))
        data = self.__socket.recv(self.buffersize).decode('utf-8')
        if data == 'ok':
            threading.Thread(target = self.__play, name = 'playX').start()
            threading.Thread(target = self.__screenshot_receive, name = 'screenshot_receiveX').start()
            print('screen开始运行...')
            self.__root.mainloop()


    def run(self):
        if self.isprick == True:
            self.run_prick()
        else:
            self.run_normal()




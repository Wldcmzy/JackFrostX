import socket
import threading
from tkinter import *
from io import BytesIO
from PIL import ImageTk, Image

class ScreenClient:
    def __init__(
        self, 
        addr: tuple[str, int] = ('127.0.0.1', 27013),
        buffersize: int = 2**20,
        screensize: tuple[int, int] = (1440, 810)
        ) -> None:

        self.__root = Tk()
        self.__root.resizable(0, 0)
        self.__root.title('JackFrostX')
        self.__lebel = Label(self.__root, image = None)
        self.screensize = screensize
        self.temp = None

        self.host, self.port = addr
        self.buffersize = buffersize
        self.__pool = []

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__lock = threading.Lock()
        

    def __screenshot_receive(self):
        while True:
            data = self.__socket.recv(self.buffersize)
            self.__pool.append(data)
    
    def __play(self):
        self.__lebel.pack()
        while True:
            if len(self.__pool) > 0:
                frame = self.__pool.pop(0)
                img = ImageTk.PhotoImage(Image.open(BytesIO(frame)).resize(self.screensize))
                self.__lebel.configure(image=img)
                self.temp = img
    
    def run(self):
        self.__socket.connect((self.host, self.port))
        threading.Thread(target = self.__play, name = 'playX').start()
        threading.Thread(target = self.__screenshot_receive, name = 'udp_screenshot_receiveX').start()
        self.__root.mainloop()






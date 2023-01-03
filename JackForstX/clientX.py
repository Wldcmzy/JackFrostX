import socket
import threading
from tkinter import *
from io import BytesIO
from PIL import ImageTk, Image

class Client:
    def __init__(
        self, 
        tcp_addr: tuple[str, int], 
        udp_addr: tuple[str, int] = ('0.0.0.0', 27014),
        buffersize: int = 2**20,
        ) -> None:
        '''
        tcp_addr: 要链接远程主机的ip端口
        udp_addr: 本地在对应ip端口开启upd监听
        '''
        self.__root = Tk()
        self.__lebel = Label(self.__root, image = None)
        self.temp = None

        self.tcp_ip, self.tcp_port = tcp_addr
        self.udp_ip, self.udp_port = udp_addr
        self.buffersize = buffersize
        self.__pool = []

        self.__tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.__lock = threading.Lock()
        

    def __screenshot_receive(self):
        while True:
            data, addr = self.__udp_socket.recvfrom(self.buffersize)
            self.__pool.append(data)
    
    def __play(self):
        self.__lebel.pack()
        while True:
            if len(self.__pool) > 0:
                frame = self.__pool.pop(0)
                img = ImageTk.PhotoImage(Image.open(BytesIO(frame)).resize((1280,720)))
                self.__lebel.configure(image=img)
                self.temp = img
    
    def __keyboard_send(self):
        while True:
            pass
    
    def run(self):
        self.__udp_socket.bind((self.udp_ip, self.udp_port))
        self.__tcp_socket.connect((self.tcp_ip, self.tcp_port))
        self.__tcp_socket.send(str(self.udp_port).encode('utf-8'))
        print('send ok')
        threading.Thread(target = self.__play, name = 'playX').start()
        threading.Thread(target = self.__screenshot_receive, name = 'udp_screenshot_receiveX').start()
        threading.Thread(target = self.__keyboard_send, name = 'tcp_keyboard_sendX').start()
        self.__root.mainloop()






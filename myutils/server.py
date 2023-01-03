from tkinter import *
import socket
import threading
from io import BytesIO
from PIL import ImageTk, Image

class Server():
    def __init__(self, host: str, port: int, buffersize: int = 4096, number: int = 2):
        self.root = Tk()
        self.lebel = Label(self.root, image = None)
        self.buffersize = buffersize
        self.temp = None #用于延迟帧对象销毁
        
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((host, port))
        self.serverSocket.listen(number)

        self.__pool = []

    def __task(self, sk: socket.socket):
        sk.send('冰冻双侠!'.encode('utf-8'))
        while True:
            data = sk.recv(self.buffersize)
            self.__pool.append(data)

    def image_auto_change(self):
        counter = 0
        while True:
            counter += 1
            # time.sleep(1/60)
            if len(self.__pool) > 0:
                try:
                    frame = self.__pool.pop(0)
                    img = ImageTk.PhotoImage(Image.open(BytesIO(frame)))
                    self.lebel.configure(image=img)
                    self.temp = img
                except:
                    print(counter)
        
    def run(self):
        print('等待客户端链接...')
        sk, addr = self.serverSocket.accept()

        task = threading.Thread(target = self.__task, args=(sk, ), name = 'tcp_task')
        task.start()

        print(f"客户端: {addr} 链接...")

        self.lebel.pack()

        t = threading.Thread(target = self.image_auto_change, name = 'autochange')
        t.start()
        print('ok')
        self.root.mainloop()



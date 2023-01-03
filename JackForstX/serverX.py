import socket
import time
import threading
from .eventAPI import (
    screenshot,
)

class Server:
    def __init__(
        self, 
        addr: tuple[str, int] = ('0.0.0.0', 27013),
        tcp_buffersize: int = 2048, 
        udp_buffersize: int = 2**20,
        listenumber: int = 1
        ) -> None:
        self.host, self.port = addr
        self.tcp_buffersize = tcp_buffersize
        self.udp_buffersize = udp_buffersize
        self.listenumber = listenumber

        self.__tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, self.udp_buffersize)
        # self.sk.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, buffersize)


    def __screenshot_send(self, ip: str, port: int):
        while True:
            time.sleep(1/20)
            frame = screenshot()
            self.__udp_socket.sendto(frame, (ip, port))
    
    def __keyboard_receive(self, sk: socket.socket):
        while True:
            data = sk.recv(self.tcp_buffersize)
            pass

    def run(self):
        self.__tcp_socket.bind((self.host, self.port))
        self.__tcp_socket.listen(self.listenumber)
        while True:
            sk, addr = self.__tcp_socket.accept()
            print(f"客户端: {addr} 链接...")
            data = sk.recv(self.tcp_buffersize).decode('utf-8')
            ip, port = addr[0], int(data)
            print(ip, port)
            threading.Thread(target = self.__keyboard_receive, args=(sk, ), name = 'keyboard_receive').start()
            threading.Thread(target = self.__screenshot_send, args=(ip, port), name = 'screenshot_send').start()

import socket
import threading

class PrickerServer:
    def __init__(
        self,
        buffersize: int,
        addr: tuple[str, int],
    ) -> None:
        self.host, self.port = addr
        self.listenumber = 2
        self.buffersize = buffersize
        self.receiver_connected = False

        self.__pool = []

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __for_receiver(self, sk: socket.socket):
        self.receiver_connected = True
        while True:
            if len(self.__pool) > 0:
                data = self.__pool.pop(0)
                sk.send(data)
                print(f'lenpool = {len(self.__pool)}  lendata = {len(data)}')

    def __for_sender(self, sk: socket.socket):
        while True:
            data = sk.recv(self.buffersize)
            if self.receiver_connected == True and len(self.__pool) < 100:
                self.__pool.append(data)
                print(str(len(data)) + '<<')

    def __keyboard_pricker(self, sk: socket.socket):
        data = sk.recv(self.buffersize).decode('utf-8')
        if data == 'receive':
            sk.send('ok'.encode('utf-8'))
            self.__for_receiver(sk)
        if data == 'send':
            sk.send('ok'.encode('utf-8'))
            self.__for_sender(sk)

    def run(self):
        self.__socket.bind((self.host, self.port))
        self.__socket.listen(self.listenumber)

        while True:
            sk, addr = self.__socket.accept()
            print(f'{addr}已连接...')
            threading.Thread(target = self.__keyboard_pricker, args=(sk, ), name = 'keyboard_pricker').start()

import socket
import keyboard

class KeyboardClient:
    def __init__(
        self, 
        addr: tuple[str, int] = ('127.0.0.1', 27014),
        buffersize: int = 1024,
        ) -> None:
        self.host, self.port = addr
        self.buffersize = buffersize

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__keyboard = {
            'w' : 'up',
            'a' : 'up',
            's' : 'up',
            'd' : 'up',
        }

    def callback(self, x):
        mode, key = x.event_type, x.name
        print(mode , key)
        print(type(mode), type(key))
        if key in self.__keyboard:
            if self.__keyboard[key] != mode:
                self.__keyboard[key] = mode
                self.__socket.send(f'{mode}:{key}#'.encode('utf-8'))
    
    def run(self):
        self.__socket.connect((self.host, self.port))
        keyboard.hook(self.callback)
        keyboard.wait()

        

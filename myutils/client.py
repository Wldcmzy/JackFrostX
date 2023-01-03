import pyautogui
from io import BytesIO
from PIL import Image
import socket
import time

class Client:
    def __init__(self, host: int, port: int):
    # def __init__(self, host: int, port: int, buffersize: int):
        self.sk = socket.socket()
        self.sk.connect((host, port))
        # self.sk.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, buffersize)
        # self.sk.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, buffersize)
        print(self.sk.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF))

    def screenshot(self) -> bytes:
        img: Image.Image = pyautogui.screenshot()
        a, b = img.size
        img = img.resize((1280, 720))
        bio = BytesIO()
        img.save(bio, format='JPEG', quality=60)
        frame = bio.getvalue()
        print(len(frame))
        return frame

    def run(self):
        while True:
            time.sleep(1/60)
            frame = self.screenshot()
            self.sk.send(frame)
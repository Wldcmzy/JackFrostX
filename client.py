from JackFrostX import ScreenClient, KeyboardClient
from JackFrostX.config import CLOUD_IP

if __name__ == '__main__':
    # # 穿透
    # kc = KeyboardClient(('127.0.0.1', 27014),prick_addr=(CLOUD_IP, 27014))
    # kc.run()
    
    # sc = ScreenClient(('127.0.0.1', 27013),prick_addr=(CLOUD_IP, 27013),screensize=(1280, 720))
    # sc.run()


    # # 直连
    kc = KeyboardClient(('127.0.0.1', 27014))
    kc.run()
    sc = ScreenClient(('127.0.0.1', 27013))
    sc.run()
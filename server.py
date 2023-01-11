from JackFrostX import ScreenServer, KeyboardServer
from JackFrostX.config import CLOUD_IP

if __name__ == '__main__':
    # # 穿透
    # ks = KeyboardServer(('0.0.0.0', 27014),prick_addr=(CLOUD_IP, 27014))
    # ks.run()
    # ss = ScreenServer(('0.0.0.0', 27013),prick_addr=(CLOUD_IP, 27013))
    # ss.run()

    # # 直连
    ks = KeyboardServer(('0.0.0.0', 27014))
    ks.run()
    ss = ScreenServer(('0.0.0.0', 27013))
    ss.run()

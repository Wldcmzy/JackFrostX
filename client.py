from JackFrostX import ScreenClient, KeyboardClient


if __name__ == '__main__':
    kc = KeyboardClient(('127.0.0.1', 27014),prick_addr=('xx.xx.xx.xx', 27014))
    kc.run()
    # 怕测试时服务器带宽不够 故缩小传送尺寸
    sc = ScreenClient(('127.0.0.1', 27013),prick_addr=('x.x.xx.x', 27013),screensize=(128, 72))
    sc.run()

    # kc = KeyboardClient(('127.0.0.1', 27014))
    # kc.run()
    # sc = ScreenClient(('127.0.0.1', 27013))
    # sc.run()
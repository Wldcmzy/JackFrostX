from JackFrostX import ScreenClient, KeyboardClient


if __name__ == '__main__':
    kc = KeyboardClient(('192.168.0.108', 27014))
    kc.run()
    # sc = ScreenClient(('192.168.0.108', 27013))
    # sc.run()
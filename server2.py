from JackFrostX import ScreenServer, KeyboardServer

if __name__ == '__main__':
    ks = KeyboardServer(('0.0.0.0', 27014))
    ks.run()
    # ss = ScreenServer(('0.0.0.0', 27013))
    # ss.run()

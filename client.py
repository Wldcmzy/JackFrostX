from myutils import Client

if __name__ == '__main__':
    HOST = '192.168.0.108'
    PORT = 33333
    c = Client(HOST, PORT)
    c.run()
from myutils import Server

if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 33333
    BUFFERSIZE = 2**20
    NUMBER = 1
    s = Server(HOST, PORT, BUFFERSIZE,NUMBER)
    s.run()
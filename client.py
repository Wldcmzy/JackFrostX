from JackForstX import Client

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 27013
    c = Client((HOST, PORT))
    c.run()
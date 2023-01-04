from JackFrostX import PrickerServer
from multiprocessing import Process

def keyboardPS():
    ps = PrickerServer(1024, ('0.0.0.0', 27014))
    ps.run()

def screenshotPS():
    ps = PrickerServer(2**20, ('0.0.0.0', 27013))
    ps.run()

if __name__ == '__main__':
    PSs = [
        Process(target=keyboardPS),
        Process(target=screenshotPS),
    ]
    for i in range(len(PSs)):
        PSs[i].start()
    
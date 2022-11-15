import socket
import time

if __name__ == '__main__':
    sfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sfd.connect(('0.0.0.0', 1238))
    
    for i in range(4):
        sfd.send(b'ping')
        t1 = time.time()
        response, addr = sfd.recv(25)
        t2 = time.time()
        response = response.decode()

        print(response)
        if response == 'ping':
            print(t2 - t1)

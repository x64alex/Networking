import socket
import time

if __name__ == '__main__':
    sfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sfd.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    for i in range(4):
        sfd.sendto(b'ping', ('172.30.255.255', 1729))
        t1 = time.time()
        response, addr = sfd.recvfrom(256)
        t2 = time.time()
        response = response.decode()

        if response == 'ping':
            print(t2 - t1)

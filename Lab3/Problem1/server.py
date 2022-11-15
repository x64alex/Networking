import socket

if __name__ == '__main__':
    sfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sfd.bind(('0.0.0.0', 1238))
    sfd.listen(256)

    while True:
        response, addr = sfd.accept()
        data = sfd.recvfrom(256)
        print(data.decode())
        sfd.sendto(response, addr)


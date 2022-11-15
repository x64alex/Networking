import socket

bind_tuple = ('0.0.0.0', 1234)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sock.connect(bind_tuple)

    send = 78
    send_string = str(send).encode()

    sock.send(send_string)

    data = sock.recv(100).decode()

    divisors = data.split(",")

    print(divisors)

    sock.close()
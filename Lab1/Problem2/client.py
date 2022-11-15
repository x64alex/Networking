import socket

BIND_TUPLE = ('0.0.0.0', 1234)

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sock.connect(BIND_TUPLE)

    string = "I love Stephanie"

    sock.send(string.encode())

    data = sock.recv(1000)

    print(data.decode())

    sock.close()
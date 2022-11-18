import socket
import time
import random

bind_tuple = ('0.0.0.0', 1221)


def encode_numbers(x, y):
    return str(x) +","+ str(y)

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(bind_tuple)

    for _ in range(0, 100):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        string = encode_numbers(x, y)
        print(x, y)
        encoded = string.encode()
        sock.send(encoded)
        data = sock.recv(1024)
        answer = data.decode()
        print(answer)

        sock.close()

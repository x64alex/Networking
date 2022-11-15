import socket
import time

bind_tuple = ('0.0.0.', 1232)

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(bind_tuple)

    time.sleep(3)
    str = "Ana has apples"
    encoded = str.encode()
    sock.send(encoded)
    data = sock.recv(1024)
    reverse = data.decode()
    print(reverse)

    sock.close()

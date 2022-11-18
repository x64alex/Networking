import socket
import threading


def decode_string(string):
    return string.split(",")

def worker(cs):
    data = cs.recv(1024).decode()
    decoded = decode_string(data)
    x = int(decoded[0])
    y = int(decoded[1])
    print(x, y)
    response = "True"
    cs.send(response.encode())
    cs.close()


bind_tuple = ('0.0.0.0', 1221)


if __name__ == "__main__":
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(bind_tuple)
        sock.listen()
    except socket.error as msg:
        print(msg)
        exit(-1)
    while True:
        client_socket, addrc = sock.accept()
        t = threading.Thread(target=worker, args=(client_socket,))
        t.start()

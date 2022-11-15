import socket
import threading
# 3.A client sends to the server a string.
# The server returns the reversed string to the client (characters from the end to begging)

def worker(cs):
    data = cs.recv(1024)
    string = data.decode()
    print(string)
    reverse = string[::-1]
    cs.send(reverse.encode())
    cs.close()
bind_tuple = ('0.0.0.', 1232)


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

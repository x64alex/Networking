import socket

ConnectionTuple = ('0.0.0.0', 1234)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(ConnectionTuple)

    string = "Goldfish"

    sock.send(string.encode())

    data = sock.recv(1000)

    reversed_String = data.decode()

    print(reversed_String)

    sock.close()



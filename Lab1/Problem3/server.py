import socket

# 3.   A client sends to the server a string.
#  The server returns the reversed string to the client (characters from the end to begging)

ConnectionTuple = ('0.0.0.0', 1234)


def reverse_string(s):
    return s[::-1]


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sock.bind(ConnectionTuple)

    sock.listen()

    while True:
        conn, addr = sock.accept()

        data = conn.recv(100).decode()
        reversed = reverse_string(data)

        print(data, reversed)

        conn.send(reversed.encode())

        conn.close()



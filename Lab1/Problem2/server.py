import socket

# 2.A client sends to the server a string. The server returns the count of spaces in the string.
BIND_TUPLE = ('0.0.0.0', 1234)


def number_of_spaces(s):
    return len(s.split())


if __name__ == "__main__":
    rdv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    rdv.bind(BIND_TUPLE)

    rdv.listen()

    while True:
        conn, addr = rdv.accept()

        data = conn.recv(400).decode()
        if not data:
            break
        print(data)
        number_spaces = number_of_spaces(data)

        send_string = str(number_spaces).encode()
        conn.send(send_string)

        conn.close()

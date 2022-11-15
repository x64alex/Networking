import socket

SERVER_PORT = 1236


def encode_array(arr):
    send_data = ""
    for el in arr:
        send_data += str(el)+","

    # Delete the last comma
    send_data = send_data[:-1]

    return send_data.encode()


if __name__ == '__main__':
    # 1.create socket
    rdv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM - tcp
    # 2. connect to the socket
    rdv.connect(('0.0.0.0', SERVER_PORT))

    arr = [1, 2, 3, 4, 5, 6, 7, 8]

    data_string = encode_array(arr)

    # 3. send
    rdv.send(data_string)

    # 4. read reply
    data = rdv.recv(100)
    print(data.decode())

    # 5. close
    rdv.close()

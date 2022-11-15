import socket

SERVER_PORT = 1236

# 1.A client sends to the server an array of numbers. Server returns the sum of the numbers.


def decode_array(data):
    arrayString = data.decode()

    array = arrayString.split(",")

    intArray = []

    for el in array:
        intArray.append(int(el))

    return intArray


def sumArray(array):

    s = 0
    for el in array:
        s += el

    return s


if __name__ == '__main__':
    # 1.Create socket
    rdv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM - tcp
    # 2.Bind socket
    rdv.bind(('0.0.0.0', SERVER_PORT))
    # 3.Listen
    rdv.listen()

    while True:
        # 4. Accept
        conn, addr = rdv.accept()

        # 5. Read
        data = conn.recv(10000)
        if not data:
            break
        # print(decode_array(data), sumArray(decode_array(data)))
        sum_array = sumArray(decode_array(data))
        data_string = str(sum_array).encode()

        # 6. Write back
        conn.send(data_string)

        # 7. Close
        conn.close()

import socket

# 5.The client sends to the server an integer. The server returns the list of divisors for the specified number.

bind_tuple = ('0.0.0.0', 1234)


def array_string(array):
    strin = ""
    for el in array:
        strin += str(el) +","

    return strin[:-1]


def get_divisors(integer):
    array = []

    for i in range(1, integer+1):
        if integer % i == 0:
            array.append(i)

    return array


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(bind_tuple)
    sock.listen()

    while True:
        comm, addr = sock.accept()

        data = comm.recv(100).decode()

        integer = int(data)

        divisors = get_divisors(integer)

        send_string = array_string(divisors)

        comm.send(send_string.encode())

        comm.close()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

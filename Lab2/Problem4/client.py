import socket
import random
import time

bind = ("0.0.0.0", 1216)


def create_string(n, array):
    string = str(n) + "##integerNumberN##"

    for el in array:
        string += str(el) + ","

    string = string[:-1]

    return string

def get_data(string):
    split = string.split('##integerNumberN##')
    n = split[0]
    array_string = split[1]
    array = array_string.split(",")

    return n, array


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(bind)

    n = int(input("Enter n:"))
    array = []

    for i in range(n):
        el = random.uniform(10.5, 75.5)
        array.append(el)

    string = create_string(n, array)
    string_encoded = string.encode()

    time.sleep(5)
    sock.send(string_encoded)

    while True:
        data = sock.recv(100000).decode()
        if data != "":
            n, array = get_data(data)
            print(n, array)
            break
        print("Waiting for response")
        time.sleep(7)

    sock.close()

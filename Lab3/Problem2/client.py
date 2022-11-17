import socket
import random
import time

bindTuple = ('0.0.0.0', 1234)

low = 1
high = 10000

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        number = random.randint(low, high)
        string_number = str(number).encode()
        time.sleep(1)
        sock.sendto(string_number, bindTuple)
        recv = sock.recv(1000)
        string = recv.decode()

        if string == "H":
            low = number
        elif string == "S":
            high = number
        elif string == "L":
            print("I lost")
            break
        else:
            print("I won")
            break

    sock.close()
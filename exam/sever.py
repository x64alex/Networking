import socket
import threading
import random
import struct
import time

random.seed()
start = 1
stop = 2**17-1
my_num = random.randint(start, stop)
print('Server number: ', my_num)
mylock = threading.Lock()
client_guessed = False
winner_thread = 0
e = threading.Event()
e.clear()
threads = []
incircle = 0
outcircle = 0
client_count = 0

def decode_string(string):
    return string.split(",")

def algorithm(x, y):
    return x*x + y*y <= 100*100

def worker(cs):
    global mylock, incircle,outcircle, my_num, winner_thread, client_count,e

    my_idcount=client_count
    print('client #',client_count,'from: ',cs.getpeername(), cs )
    message='Hello client #'+str(client_count)+' ! You are entering the number guess competion now !'
    cs.sendall(bytes(message,'ascii'))

    for i in range(0, 100):
        try:
            data = cs.recv(1024).decode()
            decoded = decode_string(data)
            x = int(decoded[0])
            y = int(decoded[1])
            print(x, y)
            is_in_circle = algorithm(x, y)
            response = str(is_in_circle)
            cs.send(response.encode())
            mylock.acquire()
            if is_in_circle:
                incircle += 1
            else:
                outcircle += 1
            print(incircle, outcircle)
            mylock.release()

        except socket.error as msg:
            print('Error:', msg.strerror)
            break


if __name__ == '__main__':
    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rs.bind(('0.0.0.0', 1234))
        rs.listen()
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)
    while True:
        client_socket, addrc = rs.accept()
        t = threading.Thread(target=worker, args=(client_socket,))
        threads.append(t)
        client_count += 1
        t.start()

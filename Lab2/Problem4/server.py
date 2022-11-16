# 4.The clients send an integer number N and an array of N float values.
# The server will merge sort the numbers received from all clients until it gets an empty array of floats (N=0).
# The server returns to each client the size of the merge-sorted array
# followed by the merge-sorted arrays of all floats from all clients.
import socket
import random

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
e = threading.Event()
e.clear()
threads = []
floats = []
finished = False
client_count = 0


def get_data(string):
    split = string.split('##integerNumberN##')
    n = split[0]
    array_string = split[1]
    array = array_string.split(",")

    return n, array


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

def merge(arr1, arr2):
    arr = []
    for c in arr1:
        arr.append(c)
    for c in arr2:
        arr.append(c)

    bubble_sort(arr)

    return arr

def create_string(n, array):
    string = str(n) + "##integerNumberN##"

    for el in array:
        string += str(el) + ","

    string = string[:-1]

    return string

def worker(cs):
    global mylock, finished, my_num, floats, client_count, e

    data = cs.recv(10000).decode()

    if len(data.split('##integerNumberN##')) == 1:
        print("Done receiving")
        finished = True
    else:
        n, array = get_data(data)
        print(n, array)
        floats = merge(floats, array)
        print(floats)

    while not finished:
        time.sleep(1)

    if finished:
        string = create_string(len(floats), floats)
        cs.send(string.encode())
        e.set()

    time.sleep(1)
    cs.close()


def resetSrv():
    global mylock, my_num, threads, e, client_count
    while True:
        e.wait()
        for t in threads:
            t.join()
        print("all threads are finished now")
        e.clear()
        mylock.acquire()
        threads = []
        my_num = random.randint(start, stop)
        print('Server number: ', my_num)
        mylock.release()

bind = ("0.0.0.0", 1216)


if __name__ == "__main__":
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(bind)
        sock.listen()
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)
    t = threading.Thread(target=resetSrv, daemon=True)
    t.start()
    while True:
        client_socket, addrc = sock.accept()
        t = threading.Thread(target=worker, args=(client_socket,))
        threads.append(t)
        client_count += 1
        t.start()







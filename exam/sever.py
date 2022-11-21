import socket
import threading
import random
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
incircle = 0
outcircle = 0
client_count = 0

def decode_string(string):
    return string.split(",")

def algorithm(x, y):
    return x*x + y*y <= 100*100

def worker(cs):
    global mylock, incircle,outcircle, my_num, winner_thread, client_count,e

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

    cs.close()

def worker2(sfd):
    global incircle, outcircle
    number = 3.14
    while True:
        mylock.acquire()
        if outcircle != 0:
            number = incircle / outcircle

        mylock.release()
        print(number)
        sfd.sendto(str(number).encode(), ('127.0.0.1', 1503))
        time.sleep(2)



if __name__ == '__main__':
    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rs.bind(('0.0.0.0', 1248))
        rs.listen()

        sfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    except socket.error as msg:
        print(msg.strerror)
        exit(-1)
    while True:
        client_socket, addrc = rs.accept()
        t = threading.Thread(target=worker, args=(client_socket,))
        t.start()

        t2 = threading.Thread(target=worker2, args=(sfd,))
        t2.start()






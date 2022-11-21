import socket, threading, random, time

def encode_numbers(x, y):
    return str(x) +","+ str(y)

def udp(sfd):
    while True:
        recieved = sfd.recvfrom(1000)
        print(recieved[0].decode())
        time.sleep(2)



if __name__ == '__main__':
    try:
        s = socket.create_connection( ('localhost',1248))
        sfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sfd.bind(('127.0.0.1', 1503))


    except socket.error as msg:
        print("Error: ",msg.strerror)
        exit(-1)

    finished=False
    sr = 1; er=2**17-1
    random.seed()

    data = s.recv(1024)
    print(data.decode('ascii'))
    step_count = 0
    for _ in range(0, 100):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        string = encode_numbers(x, y)
        print(x, y)
        encoded = string.encode()
        try:
            s.send(encoded)
            answer = s.recv(1024).decode()
        except socket.error as msg:
            print('Error: ',msg.strerror)
            s.close()
            exit(-2)
        step_count+=1
        print('Sent ',answer,' Answer ')

        time.sleep(2)

        t = threading.Thread(target=udp, args=(sfd,))
        t.start()

    s.close()
    sfd.close()
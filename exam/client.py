import socket, struct, random, time

def encode_numbers(x, y):
    return str(x) +","+ str(y)

if __name__ == '__main__':
    try:
        s = socket.create_connection( ('localhost',1234))
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

    s.close()
    if answer==b'G':
        print("I am the winner with", my_num, "in", step_count, "steps")
    else:
        print("I lost after ", step_count, "tries")


# if __name__ == "__main__":
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect(bind_tuple)
#
#     for _ in range(0, 100):
#         x = random.randint(-100, 100)
#         y = random.randint(-100, 100)
#         string = encode_numbers(x, y)
#         print(x, y)
#         encoded = string.encode()
#         sock.send(encoded)
#         data = sock.recv(1024)
#         answer = data.decode()
#         print(answer)
#
#         sock.close()

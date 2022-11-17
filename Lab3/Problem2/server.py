import socket
import random

# A client server implementation in python for the number guess problem. The server chooses a random number.
# The clients connect and send numbers to server. The server returns to each client a status message:
# ‘H’ – send a larger number ‘S’ – send a lower number
# ‘G’ – you guessed my number ‘L’ – another client guessed the number. You are a looser !

bindTuple = ('0.0.0.0', 1234)

low = 1
high = 10000

clients = []

def send_l(sock, win_client):
    for client in clients:
        if client != win_client:
            sock.sendto("L".encode(),client)

# You always need an address to send to
if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(bindTuple)

    number = random.randint(low, high)
    print("The number is "+str(number))

    while True:
        received = sock.recvfrom(10000)
        recv = received[0]
        address = received[1]
        clients.append(address)
        clientNumber = int(recv.decode())
        print(clientNumber)
        if clientNumber < number:
            sock.sendto("H".encode(), address)
            print("H")
        elif clientNumber > number:
            sock.sendto("S".encode(), address)
            print("S")
        elif clientNumber == number:
            sock.sendto("G".encode(), address)
            send_l(sock, address)
            print("G")

            break

    sock.close()
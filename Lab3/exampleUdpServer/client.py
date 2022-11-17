import socket

msgFromClient = "Hello UDP Server"

bytesToSend = msgFromClient.encode()

serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

if __name__ == "__main__":
    # Create a UDP socket at client side

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Send to server using created UDP socket

    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    print(msgFromServer[0].decode())

    msg = "Message from Server {}".format(msgFromServer[0])

    print(msg)
import struct

import select
import socket

def send_client(client_socket, clients_list):
    sz = clients_list.size()
    sz = struct.pack("!I", sz)

    client_socket.send(sz)
    for client in clients_list:
        address = client[0] + ", " + str(client[1])
        client_socket.send(address)

def update_clients():
    pass


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 1234))
    sock.listen(5)

    inputs = [sock]
    outputs = []
    clients = []
    while True:
        readable, writable, exceptional = select.select(inputs,outputs,inputs)

        for fileDescriptor in readable:
            if fileDescriptor is sock:
                [cs, address] = sock.accept()
                inputs.append(cs)
                clients.append(address)

                update_clients()
            else:
                # try and catch

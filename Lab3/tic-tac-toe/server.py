import struct
import socket
import select

# Implement the Tic-tac-toe server example (see the link bellow) using UDP and TCP –only this time each
# client should contact the server just for registration.
# All communication happens directly between the peers (clients) without passing through the server.
# Each client maintains an endpoint (TCP/UDP) with the server just for learning the arrival/departure of other clients.
# You create a mesh architecture where all clients connect directly between each others.
# Server will match 2 clients to play the game

def send_clients(clients):
    if len(clients) % 2 == 1:
        print(clients[0])
        clients[0].send("Wait for opponent".encode())
    else:
        two_clients = [clients[len(clients)-2], clients[len(clients)-1]]
        send_data = ''
        for info in two_clients:
            send_data += info[0]+','+str(info[1])+';'
        send_data = send_data[:-1]
        for client in clients:
            client.send(send_data.encode())

if __name__ == '__main__':
    clients = dict() # key: tcp socket - used to send the list of clients ,
                     # values: (udp_port - udp communication happens here, ip address - communication)
    rdv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rdv.bind(('127.0.0.1', 1237))
    rdv.listen(7)

    read_sock = [rdv]
    while True:
        ready_read, _, _ = select.select(read_sock, [], [])
        for s in ready_read:
            if s is rdv:
                # we have a new client connection
                cs, addr = s.accept()
                print('new client from addr: ', addr)
                c_udpp = cs.recv(4)
                c_udpp = struct.unpack('!I', c_udpp)[0]
                clients[cs] = (addr[0], c_udpp)
                send_clients(clients)
                read_sock.append(cs)
            else:
                data = s.recv(512)
                if not data or 'quit' in data.decode().lower():
                    s.close()
                    clients.pop(s)
                    read_sock.remove(s)
                    send_clients(clients)
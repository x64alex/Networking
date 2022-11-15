import socket
import struct

bind_tuple = ('0.0.0.0',1234)

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(bind_tuple)

    sock.listen()

    comm, adr = sock.accept()

    # The size in recv must be exact
    data = comm.recv(4)

    a=0
    unpacked = struct.unpack("!H", a)
    print(unpacked)
    comm.close()

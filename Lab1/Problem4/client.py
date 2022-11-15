import socket

BindTuple = ('0.0.0.0', 1234)

def char_to_string(char):
    result = ''
    for c in char:
        result += c + ","

    return result[:-1]




if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(BindTuple)

    char1 = ['a','c','e']
    char2 = ['b','d']


    string = char_to_string(char1)+";"+char_to_string(char2)

    sock.send(string.encode())

    data = sock.recv(300).decode()

    sortedChar = data.split(",")
    print(sortedChar)

    sock.close()
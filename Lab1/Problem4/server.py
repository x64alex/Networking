# 4.   The client send to the server two sorted array of chars.
# The server will merge sort the two arrays and return the result to the client.
import socket

BindTuple = ('0.0.0.0', 1234)

def char_to_string(char):
    result = ''
    for c in char:
        result += c + ","

    return result[:-1]

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

def merge_char(char1, char2):
    char = []
    for c in char2:
        char.append(c)
    for c in char1:
        char.append(c)

    bubble_sort(char)

    return char

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind(BindTuple)

    sock.listen()

    while True:
        conn, addr = sock.accept()
        data = conn.recv(1000).decode()

        char1, char2 = data.split(";")
        char1 = char1.split(",")
        char2 = char2.split(",")

        char = merge_char(char1, char2)

        string = char_to_string(char).encode()

        conn.send(string)

        conn.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

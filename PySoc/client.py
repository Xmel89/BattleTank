from socket import *
import sys

host = 'localhost'
port = 9090
addr = (host, port)

Data = "Hi server!"
while True:
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect(addr)

    toServeData = Data

    toServeData = str.encode(toServeData)
    tcp_socket.send(toServeData)
    response = tcp_socket.recv(1024)
    toServeData = bytes.decode(toServeData)

    response = bytes.decode(response)
    print(response)


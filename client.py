from socket import *
import sys

host = 'localhost'
port = 9090
addr = (host, port)

Data = 256

def int_to_bytes(x: int) -> bytes:
    return x

def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')

while True:
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect(addr)

    toServeData = Data

    toServeData = toServeData.to_bytes(100, byteorder='big')
    tcp_socket.send(toServeData)
    response = tcp_socket.recv(1024)


    response = int.from_bytes(response, byteorder='big')
    print(response)

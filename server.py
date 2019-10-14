from socket import *
import json


port = 9090
addr = ('', port)

Data = [25, 89]
tcp_socket = socket(AF_INET, SOCK_STREAM)

#bind - связывает адрес и порт с сокетом
tcp_socket.bind(addr)

#listen - запускает прием TCP
tcp_socket.listen(2)

while True:

    #accept - принимает запрос и устанавливает соединение, (по умолчанию работает в блокирующем режиме)
    conn, addr = tcp_socket.accept()

    #recv - получает сообщение TCP
    response = conn.recv(4096)
    response = int.from_bytes(response, byteorder='big')
    toClientData = Data
    print(response)
    toClientData = json.dumps(toClientData, ensure_ascii=False).encode()
    conn.send(toClientData)
    conn.close()


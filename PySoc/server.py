from socket import *

port = 9090
addr = ('', port)
Data = "Hi Client"
tcp_socket = socket(AF_INET, SOCK_STREAM)

#bind - связывает адрес и порт с сокетом
tcp_socket.bind(addr)

#listen - запускает прием TCP
tcp_socket.listen(2)

while True:
    #accept - принимает запрос и устанавливает соединение, (по умолчанию работает в блокирующем режиме)
    conn, addr = tcp_socket.accept()

    #recv - получает сообщение TCP
    response = conn.recv(1024)
    response = bytes.decode(response)
    print(response)
    toClientData = Data
    toClientData = str.encode(toClientData)
    conn.send(toClientData)
    conn.close()


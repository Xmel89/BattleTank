from socket import *
# from Start import PzParam as a


port = 9090
addr = ('', port)

Data = 25
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
    response = int.from_bytes(response, byteorder='big')
    toClientData = Data
    print(response)
    toClientData = (toClientData).to_bytes(100, byteorder='big')
    conn.send(toClientData)
    conn.close()


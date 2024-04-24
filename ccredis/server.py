import socket
 
server = socket.socket()            # создаем объект сокета сервера
hostname = 'localhost'              # получаем имя хоста локальной машины
port = 6379                         # устанавливаем порт сервера
server.bind((hostname, port))       # привязываем сокет сервера к хосту и порту
server.listen(5)                    # начинаем прослушиваение входящих подключений
 
print("Server running")
while True:
    con, _ = server.accept()     # принимаем клиента
    data = con.recv(1024)           # получаем данные от клиента
    message = data.decode()         # преобразуем байты в строку
    print(f"Client sent: {message}")
    if (message == "PING"):
        con.send("PONG")      # отправляем сообщение клиенту
        con.close()                     # закрываем подключение
    else:
        con.send("Unknown command")
    
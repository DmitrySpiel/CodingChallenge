import socket, getopt, sys
from ccredis.serialization import define_input

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"")
    except getopt.GetoptError:
        print ('Usage: ccwc.py (-hclwm) <filename>')
        sys.exit(2)
    client = socket.socket()            # создаем сокет клиента
    hostname = 'localhost'              # получаем хост локальной машины
    port = 6379                         # устанавливаем порт сервера
    client.connect((hostname, port))    # подключаемся к серверу
    message = args[0]                   # вводим сообщение
    client.send(message.encode())       # отправляем сообщение серверу
    data = client.recv(1024)            # получаем данные с сервера
    print("Server sent: ", data.decode()) 
    client.close()                      # закрываем подключение
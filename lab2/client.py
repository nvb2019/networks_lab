import socket

shutdown = False
join = False

host = socket.gethostbyname(socket.gethostname())
port = 0

server = ('127.0.1.1', 8080)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

message = input('Введите сообщение: ')

if message:
    s.sendto(message.encode('utf-8'), server)

s.close()

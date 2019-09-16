import socket
from string import ascii_letters
from random import randint

shutdown = False
join = False

host = socket.gethostbyname(socket.gethostname())
port = 0

server = ('127.0.1.1', 8080)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)
message = ' '.join([''.join([ascii_letters[randint(0, 25)] for i in range(randint(3, 10))]) for i in range(100)])

if message:
    s.sendto(message.encode('utf-8'), server)

s.close()

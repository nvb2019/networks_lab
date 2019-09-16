import socket

shutdown = False
join = False

host = socket.gethostbyname(socket.gethostname())
port = 0

server = ('127.0.1.1', 8080)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

with open('binary_file.png', 'rb') as f:
    binary_file = f.read(1024)
    while binary_file:
        s.sendto(binary_file, server)
        binary_file = f.read(1024)
print('done sending')

s.close()

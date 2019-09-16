import socket, time

host = socket.gethostbyname(socket.gethostname())
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

f = open('test/new_file.png', 'wb')

clients = []

quit = False
print('[ Server Started ]')

while not quit:
    try:
        data, addr = sock.recvfrom(1024)
        while data:
            f.write(data)
            data, addr = sock.recvfrom(1024)
        f.close()
    except:
        print('[ Server Stopped ]')
        quit = True

sock.close()

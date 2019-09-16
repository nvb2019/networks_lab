import socket, time

host = socket.gethostbyname(socket.gethostname())
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

clients = []

quit = False
print('[ Server Started ]')

while not quit:
    try:
        data, addr = sock.recvfrom(1024)
    except:
        print('[ Server Stopped ]')
        quit = True
    else:
        print(data.decode('utf-8'))

sock.close()

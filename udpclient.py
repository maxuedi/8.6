import socket

udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

address = ("127.0.0.1",7001)

udpSocket.sendto(b"hello",address)

data = udpSocket.recv(1024)
print(data.decode())

udpSocket.close()
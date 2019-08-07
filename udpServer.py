import socket
time = 0
s = 0
#新建一个udp socket
udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#绑定窗口
udpSocket.bind(("0.0.0.0",7001))

print(f"bind 7001....")
#接受和发送
while True:
    #接受用 recvfrom
    recv_data,client_address = udpSocket.recvfrom(1024)
    print(f"从{client_address}接受的数据：{recv_data}")
    time = time + 1
    s = s + len(recv_data)
    #发送sendto
    data = f"接收到{time}次数据,总字节数为{s},这次数据为{recv_data}"
    udpSocket.sendto(data.encode(),client_address)

    #关闭连接
    # udpSocket.close()
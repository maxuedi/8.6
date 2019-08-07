import socket
time = 0
s = 0
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('0.0.0.0', 8000)
server_sock.bind(address)
#print(f"bind{address}......")

server_sock.listen(10)

while True:
    #等待连接
    conn,addr = server_sock.accept()
    print(f"{addr}connected!")
    recv_data = conn.recv(1024)
    if recv_data == b"": 
        conn.close()
    print(f"接收到数据:{recv_data}")
    time = time + 1
    s = s + len(recv_data)
    data = f"接收到{time}次数据,总字节数为{s},这次数据为{recv_data}"
    conn.send(data.encode())
    conn.close()

server_sock.close()




import socket

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(('192.168.40.42', 3176))
tcp_server_socket.listen(128)
while True:  # 新的客户端加入
    con_tcp_server_socket, client_adr = tcp_server_socket.accept()
    while True:  # 重复回答
        client_massage = con_tcp_server_socket.recv(1024)
        if len(client_massage) == 0:
            print('客户端结束了')
            break
        else:
            print(f"{client_adr},{client_massage.decode('utf8')}")
            data = input('请回复:')
            con_tcp_server_socket.send(data.encode('utf8'))

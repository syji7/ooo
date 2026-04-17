import socket

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect(('192.168.40.187', 8080))
while True:
    data = input('输入:')
    tcp_client_socket.send(data.encode('utf8'))
    server_massage = tcp_client_socket.recv(1024)
    if len(server_massage) == 0:
        break
    else:
        print(f"回复消息:{server_massage.decode('utf8')}")

tcp_client_socket.close()

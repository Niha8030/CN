import socket

serverName = '192.168.43.179'
serverPort = 12001
# create
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind
server_socket.bind((serverName, serverPort))

# listen
server_socket.listen(1)

while True:
    print("Server waiting for connection")
    client_socket, addr = server_socket.accept()
    print("Client connected from", addr)
    sentence = client_socket.recv(1024).decode()

    file = open(sentence, "r")
    l = file.read(1024)

    client_socket.send(l.encode())
    file.close()
    client_socket.close()

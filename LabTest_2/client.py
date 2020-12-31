import socket

serverName = '192.168.43.179'
serverPort = 12001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((serverName, serverPort))
sentence = input("Enter file name: ")

client_socket.send(sentence.encode())
filecontents = client_socket.recv(1024).decode()
print('From Server:', filecontents)
client_socket.close()

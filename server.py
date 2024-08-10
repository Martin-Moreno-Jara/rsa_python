import socket
import threading

HOST = socket.gethostbyname(socket.gethostname()) #'127.0.0.1'  
PORT = 9090

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(2)

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client:socket.socket):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


def receiveConnection():
    while True:
        print('hello')
        client, address = server.accept()
        print(f"connected with {str(address)}")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)

        clients.append(client)
        nicknames.append(nickname)

        print(f"nickname of the client is {nickname}")
        broadcast(f"{nickname} connected to the chat\n".encode('utf-8'))

        client.send('Connected to the server'.encode('utf-8'))

        thread = threading.Thread(target=handle,args=(client,))
        thread.start()

print('server running')
receiveConnection()
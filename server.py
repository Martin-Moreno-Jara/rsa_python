import socket
import threading
import time

HOST = socket.gethostbyname(socket.gethostname()) #'127.0.0.1'  
PORT = 9090

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(2)

clients = []
nicknames = []
pkeys = []
ns = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client:socket.socket):
    while True:
        try:
            message = client.recv(1024)
            if client==clients[0]:
                clients[1].send(message)
            elif client==clients[1]:
                clients[0].send(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


def receiveConnection():
    while True:
        client, address = server.accept()
        print(f"connected with {str(address)}")

        client.send("NICK".encode())
        nickname = client.recv(1024)

        clients.append(client)
        nicknames.append(nickname)

        client.send("EANDN".encode())
        public_partner = client.recv(1024).decode()
        partner_n = client.recv(1024).decode()

        pkeys.append(public_partner)
        ns.append(partner_n)

        print(public_partner)
        print(partner_n)

        print(f"nickname of the client is {nickname}")

        # time.sleep(2)
        # broadcast(f"{nickname} connected to the chat\n".encode())
        # client.send('Connected to the server\n'.encode())

        if len(clients)==2:
            time.sleep(1)
            clients[0].send(f"GETKEYS {pkeys[1]} {ns[1]}".encode())
            clients[1].send(f"GETKEYS {pkeys[0]} {ns[0]}".encode())

        thread = threading.Thread(target=handle,args=(client,))
        thread.start()

print('server running')
receiveConnection()
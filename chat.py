from rsa_imp import rsa_imp
import socket
import threading

rsa = rsa_imp()

public_key = rsa.generateKeys()
public_partner, partner_n = None, None

print(public_key)

choice:str = input('host (1) or connect (2): ')

if choice == '1':
    print(f'you are hosting {public_key}')
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(("192.168.20.6",5029))
    server.listen()

    client, _ = server.accept()
    client.send(public_key.to_bytes(1024,"big"))
    client.send(rsa.n.to_bytes(1024,"big"))
    public_partner = int.from_bytes(client.recv(1024),"big") 
    partner_n = int.from_bytes(client.recv(1024),'big')
    print(f'1 partner: {public_partner}')
elif choice == '2':
    print(f'you are connecting {public_key}')
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("192.168.20.6",5029))
    public_partner = int.from_bytes(client.recv(1024),"big") 
    partner_n = int.from_bytes(client.recv(1024),'big')
    client.send(public_key.to_bytes(1024,'big'))
    client.send(rsa.n.to_bytes(1024,"big"))
    print(f'2 partner: {public_partner}')
else:
    exit()


def send_message(client):
    while True:
        message = input("")
        client.send(rsa.encrypt(message,public_partner,partner_n).encode())
        print(f'you: {message} ')

def send_message_ne(client):
    while True:
        message = input("")
        client.send(message.encode())
        print(f'you: {message} ')

def receive_message(c):
    while True:
        decoded = c.recv(1024).decode()
        decryptes = rsa.decrypt(decoded)
        print(f'parnter: {decryptes}')
        #print(f'partner: { rsa.decrypt(c.recv(1024)).decode()} ')
def receive_message_ne(c):
    while True:
        decoded = c.recv(1024).decode()
        print(f'parnter: {decoded}')

#ENCRYPTED
threading.Thread(target=send_message, args=(client,)).start()
threading.Thread(target=receive_message, args=(client,)).start()
# NOT ENCRYPTED 
# threading.Thread(target=send_message_ne, args=(client,)).start()
# threading.Thread(target=receive_message_ne, args=(client,)).start()
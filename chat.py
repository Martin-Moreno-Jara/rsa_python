import rsa
import socket
import threading

public_key, private_key = rsa.newkeys(1024)
public_partner = None

choice:str = input('host (1) or connect (2): ')

if choice == '1':
    print('you are hosting')
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(("192.168.20.6",5029))
    server.listen()

    client, _ = server.accept()
    client.send(public_key.save_pkcs1("PEM"))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
elif choice == '2':
    print('you are connecting')
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("192.168.20.6",5029))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1("PEM"))
else:
    exit()


def send_message(client):
    while True:
        message = input("")
        client.send(rsa.encrypt(message.encode(),public_partner))
        print(f'you: {message} ')

def receive_message(c):
    while True:
        print(f'partner: { rsa.decrypt(c.recv(1024), private_key).decode()} ')

threading.Thread(target=send_message, args=(client,)).start()
threading.Thread(target=receive_message, args=(client,)).start()

# from rsa_imp import rsa_imp
# import socket
# import threading

# rsa = rsa_imp()

# public_key = rsa.generateKeys()
# public_partner, partner_n = None, None

# print(public_key)

# choice:str = input('host (1) or connect (2): ')

# if choice == '1':
#     print(f'you are hosting {public_key}')
#     server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     server.bind(("192.168.1.11",9999))
#     server.listen()

#     client, _ = server.accept()
#     client.send(public_key.to_bytes(1024,"big"))
#     client.send(rsa.n.to_bytes(1024,"big"))
#     public_partner = int.from_bytes(client.recv(1024),"big") 
#     partner_n = int.from_bytes(client.recv(1024),'big')
#     print(f'1 partner: {public_partner}')
# elif choice == '2':
#     print(f'you are connecting {public_key}')
#     client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     client.connect(("192.168.1.11",9999))
#     public_partner = int.from_bytes(client.recv(1024),"big") 
#     partner_n = int.from_bytes(client.recv(1024),'big')
#     client.send(public_key.to_bytes(1024,'big'))
#     client.send(rsa.n.to_bytes(1024,"big"))
#     print(f'2 partner: {public_partner}')
# else:
#     exit()


# def send_message(client):
#     while True:
#         message = input("")
#         client.send(rsa.encrypt(message,public_partner,partner_n).encode())
#         print(f'you: {message} ')

# def send_message_ne(client):
#     while True:
#         message = input("")
#         client.send(message.encode())
#         print(f'you: {message} ')

# def receive_message(c):
   
#         decoded = c.recv(1024).decode()
#         decryptes = rsa.decrypt(decoded)
#         print(f'parnter: {decryptes}')
#         #print(f'partner: { rsa.decrypt(c.recv(1024)).decode()} ')
# def receive_message_ne(c):
#     while True:
#         decoded = c.recv(1024).decode()
#         print(f'parnter: {decoded}')

# #ENCRYPTED
# threading.Thread(target=send_message, args=(client,)).start()
# threading.Thread(target=receive_message, args=(client,)).start()
# # # NOT ENCRYPTED 
# # # threading.Thread(target=send_message_ne, args=(client,)).start()
# # # threading.Thread(target=receive_message_ne, args=(client,)).start()

##--------------------------------------

# import tkinter as tk
# import threading
# import socket
# from rsa_imp import rsa_imp
# import sys
# import io

# # Redirigir la salida estándar (print) a la interfaz gráfica
# class RedirectText(io.StringIO):
#     def __init__(self, text_widget):
#         super().__init__()
#         self.text_widget = text_widget

#     def write(self, string):
#         self.text_widget.insert(tk.END, string)
#         self.text_widget.see(tk.END)

# def start_rsa_program(input_widget, text_widget):
#     # Redirigir la entrada estándar (input)
#     def input_prompt(prompt=""):
#         text_widget.insert(tk.END, prompt)
#         input_value = input_widget.get()
#         input_widget.delete(0, tk.END)
#         return input_value

#     rsa = rsa_imp()

#     public_key = rsa.generateKeys()
#     public_partner, partner_n = None, None

#     print(public_key)

#     choice = input_prompt('host (1) or connect (2): ')

#     if choice == '1':
#         print(f'you are hosting {public_key}')
#         server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         server.bind(("192.168.1.11", 9999))
#         server.listen()

#         client, _ = server.accept()
#         client.send(public_key.to_bytes(1024, "big"))
#         client.send(rsa.n.to_bytes(1024, "big"))
#         public_partner = int.from_bytes(client.recv(1024), "big")
#         partner_n = int.from_bytes(client.recv(1024), 'big')
#         print(f'1 partner: {public_partner}')
#     elif choice == '2':
#         print(f'you are connecting {public_key}')
#         client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         client.connect(("192.168.1.11", 9999))
#         public_partner = int.from_bytes(client.recv(1024), "big")
#         partner_n = int.from_bytes(client.recv(1024), 'big')
#         client.send(public_key.to_bytes(1024, 'big'))
#         client.send(rsa.n.to_bytes(1024, "big"))
#         print(f'2 partner: {public_partner}')
#     else:
#         return

#     def send_message(client):
#         while True:
#             message = input_prompt("")
#             client.send(rsa.encrypt(message, public_partner, partner_n).encode())
#             print(f'you: {message} ')

#     def receive_message(c):
#         while True:
#             decoded = c.recv(1024).decode()
#             decrypted = rsa.decrypt(decoded)
#             print(f'partner: {decrypted}')

#     threading.Thread(target=send_message, args=(client,)).start()
#     threading.Thread(target=receive_message, args=(client,)).start()

# def main():
#     # Crear la ventana principal
#     root = tk.Tk()
#     root.title("RSA Chat")

#     # Crear un widget Text para mostrar la salida (print)
#     text_output = tk.Text(root, height=20, width=50)
#     text_output.pack(pady=10)

#     # Redirigir el print a la interfaz gráfica
#     sys.stdout = RedirectText(text_output)

#     # Crear un cuadro de entrada de texto
#     entry_input = tk.Entry(root, width=50)
#     entry_input.pack(pady=10)

#     # Crear un botón para iniciar el programa RSA
#     start_button = tk.Button(root, text="Start", command=lambda: threading.Thread(target=start_rsa_program, args=(entry_input, text_output)).start())
#     start_button.pack(pady=10)

#     # Iniciar el bucle principal de la aplicación
#     root.mainloop()

# if __name__ == "__main__":
#     main()

# import tkinter as tk
# from tkinter import scrolledtext
# from rsa_imp import rsa_imp
# import socket
# import threading
# import queue

# # Configuración de RSA y sockets
# rsa = rsa_imp()
# public_key = rsa.generateKeys()
# public_partner, partner_n = None, None
# client = None
# message_queue = queue.Queue()

# def setup_connection():
#     global public_partner, partner_n, client
#     choice = choice_var.get()

#     if choice == '1':
#         output_text.insert(tk.END, f'You are hosting {public_key}\n')
#         server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         server.bind(("192.168.1.11", 9999))
#         server.listen()

#         client, _ = server.accept()
#         client.send(public_key.to_bytes(1024, "big"))
#         client.send(rsa.n.to_bytes(1024, "big"))
#         public_partner = int.from_bytes(client.recv(1024), "big")
#         partner_n = int.from_bytes(client.recv(1024), 'big')
#         output_text.insert(tk.END, f'1 partner: {public_partner}\n')
#     elif choice == '2':
#         output_text.insert(tk.END, f'You are connecting {public_key}\n')
#         client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         client.connect(("192.168.1.11", 9999))
#         public_partner = int.from_bytes(client.recv(1024), "big")
#         partner_n = int.from_bytes(client.recv(1024), 'big')
#         client.send(public_key.to_bytes(1024, 'big'))
#         client.send(rsa.n.to_bytes(1024, "big"))
#         output_text.insert(tk.END, f'2 partner: {public_partner}\n')
#     else:
#         exit()

#     # Iniciar hilos para enviar y recibir mensajes
#     threading.Thread(target=send_message, args=(client,), daemon=True).start()
#     threading.Thread(target=receive_message, args=(client,), daemon=True).start()

# def send_message(client):
#     while True:
#         message = message_entry.get()
#         if message:
#             client.send(rsa.encrypt(message, public_partner, partner_n).encode())
#             message_queue.put(f'You: {message}')
#             message_entry.delete(0, tk.END)

# def receive_message(c):
#     while True:
#         decoded = c.recv(1024).decode()
#         decrypted = rsa.decrypt(decoded)
#         message_queue.put(f'Partner: {decrypted}')

# def update_text():
#     while not message_queue.empty():
#         msg = message_queue.get()
#         output_text.config(state='normal')
#         output_text.insert(tk.END, f'{msg}\n')
#         output_text.config(state='disabled')
#         output_text.yview(tk.END)  # Desplaza la vista al final

#     root.after(100, update_text)  # Reintenta después de 100 ms

# # Configuración de la interfaz gráfica
# root = tk.Tk()
# root.title("RSA Chat")

# choice_var = tk.StringVar(value='1')

# # Configurar marco para la elección
# frame = tk.Frame(root)
# frame.pack(pady=10)

# tk.Radiobutton(frame, text="Host", variable=choice_var, value='1').pack(side=tk.LEFT)
# tk.Radiobutton(frame, text="Connect", variable=choice_var, value='2').pack(side=tk.LEFT)
# tk.Button(frame, text="Start", command=setup_connection).pack(side=tk.LEFT)

# # Configurar área de texto para mostrar mensajes
# output_text = scrolledtext.ScrolledText(root, width=50, height=20, state='disabled')
# output_text.pack(pady=10)

# # Configurar entrada de mensaje
# message_entry = tk.Entry(root, width=50)
# message_entry.pack(pady=10)

# # Iniciar actualización de la interfaz gráfica
# update_text()

# root.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
# intento PRINCIPAL GABO
# import tkinter as tk
# from tkinter import ttk
# import threading
# import socket
# from rsa_imp import rsa_imp
# import sys
# import io

# # Redirigir la salida estándar (print) a la interfaz gráfica


# def start_rsa_program(input_widget, text_widget):
#     # Redirigir la entrada estándar (input)
#     def input_prompt():
#         texto=input_widget.get()
#         text_widget.insert(tk.END, texto + "\n")
        
#         input_widget.delete(0, tk.END)
#         return texto


#     rsa = rsa_imp()

#     public_key = rsa.generateKeys()
#     public_partner, partner_n = None, None

#     print(public_key)

#     text_widget.insert(tk.END,'host (1) or connect (2): ')
#     choice = input_prompt()
#     text_public_key=str(public_key)
#     text_public_partner=str(public_partner)
#     if choice == '1':
       
#         text_widget.insert(tk.END,'You are hosting'+ text_public_key)
#         print(f'You are hosting {public_key}')
#         server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         server.bind(("192.168.20.86", 9999))
#         server.listen()

#         client, _ = server.accept()
#         client.send(public_key.to_bytes(1024, "big"))
#         client.send(rsa.n.to_bytes(1024, "big"))
#         public_partner = int.from_bytes(client.recv(1024), "big")
#         partner_n = int.from_bytes(client.recv(1024), 'big')
#         text_widget.insert(tk.END,'1 partner'+ text_public_partner)
#         print(f'1 partner: {public_partner}')
#     elif choice == '2':
#         print(f'You are connecting {public_key}')
#         text_widget.insert(tk.END,'You are connecting'+ text_public_key)
#         client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         client.connect(("192.168.20.86", 9999))
#         public_partner = int.from_bytes(client.recv(1024), "big")
#         partner_n = int.from_bytes(client.recv(1024), 'big')
#         client.send(public_key.to_bytes(1024, 'big'))
#         client.send(rsa.n.to_bytes(1024, "big"))
#         print(f'2 partner: {public_partner}')
#         text_widget.insert(tk.END,'2 partner'+ text_public_partner)
#     else:
#         return

#     def send_message(client):
#         while True:
#           #  text_widget.insert(tk.END,'You')
#             hola=input("")
#             message = input_prompt()
#             client.send(rsa.encrypt(message, public_partner, partner_n).encode())
#             print(f'You: {message}')
           

#     def receive_message(c):
#         while True:
#             text_widget.insert(tk.END,'Partner')
#             decoded = c.recv(1024).decode()
#             decrypted = rsa.decrypt(decoded)
#             print(f'Partner: {decrypted}')

#     threading.Thread(target=send_message, args=(client,), daemon=True).start()
#     threading.Thread(target=receive_message, args=(client,), daemon=True).start()

# def main():
#     # Crear la ventana principal
#     root = tk.Tk()
#     root.title("RSA Chat")
#     root.geometry("600x400")
#     root.configure(bg='#e0f0ff')

#     # Crear un marco para organizar los widgets
#     main_frame = tk.Frame(root, bg='#e0f0ff')
#     main_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

#     # Crear un widget Text para mostrar la salida (print)
#     text_output = tk.Text(main_frame, height=15, width=70, bg='#f0f8ff', fg='#000000', wrap=tk.WORD, font=('Arial', 12))
#     text_output.pack(pady=10, fill=tk.BOTH, expand=True)

#     # Redirigir el print a la interfaz gráfica


#     # Crear un cuadro de entrada de texto
#     entry_input = tk.Entry(main_frame, width=70, font=('Arial', 12))
#     entry_input.pack(pady=10)

#     # Crear un botón para iniciar el programa RSA
#     start_button = ttk.Button(main_frame, text="Start", command=lambda: threading.Thread(target=start_rsa_program, args=(entry_input, text_output), daemon=True).start())
#     start_button.pack(pady=10)



#     # Iniciar el bucle principal de la aplicación
#     root.mainloop()



# if __name__ == "__main__":
#     main()
#---------------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
import threading
import socket
from rsa_imp import rsa_imp
import sys
import io
import time

# Redirigir la salida estándar (print) a la interfaz gráfica

def input_prompt(input_widget, text_widget):
        texto=input_widget.get()
        text_widget.insert(tk.END, texto + "\n")
        
        input_widget.delete(0, tk.END)
        return texto

def start_rsa_program(input_widget, text_widget):
    # Redirigir la entrada estándar (input)
    

    rsa = rsa_imp()

    public_key = rsa.generateKeys()
    public_partner, partner_n = None, None

    print(public_key)

    text_widget.insert(tk.END,'host (1) or connect (2): ')
    choice = input_prompt(input_widget, text_widget)
    text_public_key=str(public_key)
    text_public_partner=str(public_partner)
    if choice == '1':
       
        text_widget.insert(tk.END,'You are hosting'+ text_public_key)
        print(f'You are hosting {public_key}')
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("192.168.20.86", 9999))
        server.listen()

        client, _ = server.accept()
        client.send(public_key.to_bytes(1024, "big"))
        client.send(rsa.n.to_bytes(1024, "big"))
        public_partner = int.from_bytes(client.recv(1024), "big")
        partner_n = int.from_bytes(client.recv(1024), 'big')
        text_widget.insert(tk.END,'1 partner'+ text_public_partner+'\n')
        print(f'1 partner: {public_partner}')
    elif choice == '2':
        print(f'You are connecting {public_key}')
        text_widget.insert(tk.END,'You are connecting'+ text_public_key)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("192.168.20.86", 9999))
        public_partner = int.from_bytes(client.recv(1024), "big")
        partner_n = int.from_bytes(client.recv(1024), 'big')
        client.send(public_key.to_bytes(1024, 'big'))
        client.send(rsa.n.to_bytes(1024, "big"))
        print(f'2 partner: {public_partner}')
        text_widget.insert(tk.END,'2 partner'+ text_public_partner)
    else:
        return

    def send_message(client):
        while True:
            time.sleep(10)
            text_widget.insert(tk.END,'You: ')
            message = input_prompt(input_widget, text_widget)
            text_widget.insert(tk.END,'\n')
            client.send(rsa.encrypt(message, public_partner, partner_n).encode())
            print(f'You: {message}')

    def receive_message(c):
        while True:
           # text_widget.insert(tk.END,'Partner: ')
            decoded = c.recv(1024).decode()
            decrypted = rsa.decrypt(decoded)
            text_widget.insert(tk.END,'Partner:'+decrypted+'\n')
            print(f'Partner: {decrypted}')

    threading.Thread(target=send_message, args=(client,), daemon=True).start()
    threading.Thread(target=receive_message, args=(client,), daemon=True).start()

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("RSA Chat")
    root.geometry("600x400")
    root.configure(bg='#e0f0ff')

    # Crear un marco para organizar los widgets
    main_frame = tk.Frame(root, bg='#e0f0ff')
    main_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Crear un widget Text para mostrar la salida (print)
    text_output = tk.Text(main_frame, height=15, width=70, bg='#f0f8ff', fg='#000000', wrap=tk.WORD, font=('Arial', 12))
    text_output.pack(pady=10, fill=tk.BOTH, expand=True)

    # Redirigir el print a la interfaz gráfica


    # Crear un cuadro de entrada de texto
    entry_input = tk.Entry(main_frame, width=70, font=('Arial', 12))
    entry_input.pack(pady=10)

    # Crear un botón para iniciar el programa RSA
    start_button = ttk.Button(main_frame, text="Start", command=lambda: threading.Thread(target=start_rsa_program, args=(entry_input, text_output), daemon=True).start())
    start_button.pack(pady=10)

    continue_button = ttk.Button(main_frame, text="Contnue", command=lambda:input_prompt(entry_input, text_output))
    continue_button.pack(pady=10)

  
    # Iniciar el bucle principal de la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
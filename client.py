import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog
from rsa_imp import rsa_imp
HOST = socket.gethostbyname(socket.gethostname()) #'127.0.0.1' 
PORT = 9090

class Client:

    def __init__(self,host,port):
        self.rsa:rsa_imp = rsa_imp()

        self.public_key = self.rsa.generateKeys()
        self.public_partner, self.partner_n = None, None

        print('my e ',self.public_key)
        print('my n ',self.rsa.n)

        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((host,port))

        msg = tkinter.Tk()
        msg.withdraw()

        self.nickname = simpledialog.askstring('Nickname',"please choose a nickname",parent=msg)

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()
    
    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg='lightgray')

        self.chat_label = tkinter.Label(self.win,text='Chat:',bg='lightgray')
        self.chat_label.config(font=("Arial",12))
        self.chat_label.pack(padx=20,pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20,pady=5)
        self.text_area.config(state='disabled')

        self.msg_label = tkinter.Label(self.win, text="Message:",bg="lightgray")
        self.msg_label.config(font=("Arial",12))
        self.msg_label.pack(padx=20,pady=5)

        self.input_area = tkinter.Text(self.win,height=3)
        self.input_area.pack(padx=20,pady=5)

        self.send_button = tkinter.Button(self.win,text="Send",command=self.write)
        self.send_button.config(font=("Arial",12))
        self.send_button.pack(padx=20,pady=5)

        self.gui_done = True

        self.win.protocol("WM_DELETE_WINDOW",self.stop)

        self.win.mainloop()
    
    def display_message(self,message):
        self.text_area.config(state='normal')
        self.text_area.insert('end',message)
        self.text_area.yview('end')
        self.text_area.config(state='disabled')

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def write(self):
        message = f"{self.nickname}: {self.input_area.get('1.0','end')}"  
        self.display_message(message)
        encriptedMessage = self.rsa.encrypt(message, self.public_partner, self.partner_n)
        self.sock.send(encriptedMessage.encode())
        self.input_area.delete('1.0','end')
    

    
    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode()
                if message == 'NICK':
                    self.sock.send(self.nickname.encode())
                elif message == 'EANDN':
                    self.sock.send(str(self.public_key).encode())
                    self.sock.send(str(self.rsa.n).encode())
                elif message.split(' ')[0] == "GETKEYS":
                    splitmessage = message.split(' ')
                    self.public_partner = int(splitmessage[1])
                    self.partner_n = int(splitmessage[2])
                    print(self.public_partner,self.partner_n)
                else:
                    if self.gui_done:
                        decrypted = self.rsa.decrypt(message)
                        self.display_message(decrypted)
      
            except ConnectionAbortedError:
                break
            except:
                print('error')
                self.sock.close()
                break

client = Client(HOST,PORT)
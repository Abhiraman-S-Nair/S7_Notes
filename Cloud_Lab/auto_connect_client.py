# client_script.py
import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox

class ClientChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat App")

        # Setup GUI
        self.chat_area = tk.Text(master, state='disabled', wrap='word')
        self.chat_area.pack(pady=10)

        self.message_entry = tk.Entry(master)
        self.message_entry.pack(fill=tk.X, padx=10, pady=5)
        self.message_entry.bind("<Return>", self.send_message)

        # Connect to the server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 55555))

        # Get username
        self.username = simpledialog.askstring("Username", "Enter your username:")
        self.client_socket.send(self.username.encode('utf-8'))

        # Start receiving messages
        self.running = True
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

    def receive_messages(self):
        while self.running:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.chat_area.config(state='normal')
                self.chat_area.insert(tk.END, message + "\n")
                self.chat_area.config(state='disabled')
                self.chat_area.yview(tk.END)
            except:
                self.running = False
                self.client_socket.close()
                break

    def send_message(self, event=None):
        message = self.message_entry.get()
        self.message_entry.delete(0, tk.END)

        if message.lower() == "exit":
            self.client_socket.send("EXIT".encode('utf-8'))
            self.running = False
            self.client_socket.close()
            messagebox.showinfo("Chat", "You have left the chat.")
            self.master.destroy()
        else:
            self.client_socket.send(message.encode('utf-8'))

# Run the client application
root = tk.Tk()
app = ClientChatApp(root)
root.mainloop()

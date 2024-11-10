import socket
import threading
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import csv

class ClientApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Client - Chat and Analysis")

        # Top window for chat messages and broadcasting
        tk.Label(master, text="Chat Messages").pack()
        self.chat_area = tk.Text(master, wrap='word', height=10, width=50, state='disabled', bg="lightgrey")
        self.chat_area.pack(pady=5)

        self.message_entry = tk.Entry(master, width=50)
        self.message_entry.pack(pady=5)

        self.broadcast_btn = tk.Button(master, text="Broadcast", command=self.broadcast_message)
        self.broadcast_btn.pack(pady=5)

        # Middle window for text analysis
        tk.Label(master, text="Text Analysis").pack()
        self.analysis_entry = tk.Entry(master, width=50)
        self.analysis_entry.pack(pady=5)

        self.send_text_btn = tk.Button(master, text="Send Text", command=self.prompt_word_and_send_text)
        self.send_text_btn.pack(pady=5)

        self.send_file_btn = tk.Button(master, text="Send File", command=self.prompt_word_and_send_file)
        self.send_file_btn.pack(pady=5)

        # Bottom window for displaying analysis results
        tk.Label(master, text="Analysis Results").pack()
        self.result_area = tk.Text(master, wrap='word', height=10, width=50, state='disabled')
        self.result_area.pack(pady=5)

        # Set up client socket connection
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(('127.0.0.1', 50000))
            threading.Thread(target=self.receive_messages).start()
        except ConnectionRefusedError:
            messagebox.showerror("Connection Error", "Unable to connect to the server.")
            self.master.destroy()

    def broadcast_message(self):
        message = self.message_entry.get()
        if message:
            self.client_socket.sendall(f"BROADCAST:{message}".encode('utf-8'))
            self.message_entry.delete(0, tk.END)

    def prompt_word_and_send_text(self):
        specific_word = simpledialog.askstring("Specific Word", "Enter the specific word to count (or type 'NONE' to skip):")
        text_data = self.analysis_entry.get().strip()
        if text_data:
            self.client_socket.sendall(f"ANALYZE_TEXT:{text_data}|{specific_word}".encode('utf-8'))

    def prompt_word_and_send_file(self):
        specific_word = simpledialog.askstring("Specific Word", "Enter the specific word to count (or type 'NONE' to skip):")
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv")])
        if file_path:
            with open(file_path, 'r') as file:
                data = file.read()
                self.client_socket.sendall(f"ANALYZE_FILE:{data}|{specific_word}".encode('utf-8'))

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(4096).decode('utf-8')
                if message.startswith("BROADCAST:"):
                    self.update_chat_area(message.replace("BROADCAST:", ""))
                elif message.startswith("RESULT:"):
                    self.update_result_area(message.replace("RESULT:", ""))
            except:
                break

    def update_chat_area(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{message}\n")
        self.chat_area.config(state='disabled')

    def update_result_area(self, result):
        self.result_area.config(state='normal')
        self.result_area.insert(tk.END, f"{result}\n")
        self.result_area.config(state='disabled')

# Run the client application
root = tk.Tk()
app = ClientApp(root)
root.mainloop()

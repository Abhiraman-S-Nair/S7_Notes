import socket
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import threading


class ClientApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File/Text Sender")

        # Text area for user input
        self.text_area = tk.Text(master, wrap='word', height=10, width=50)
        self.text_area.pack(pady=10)

        # Buttons for sending text and file
        self.send_text_btn = tk.Button(master, text="Send Text", command=self.prompt_word_and_send_text)
        self.send_text_btn.pack(pady=5)

        self.send_file_btn = tk.Button(master, text="Send File", command=self.prompt_word_and_send_file)
        self.send_file_btn.pack(pady=5)

        # Text area for displaying results from the server
        self.result_area = tk.Text(master, wrap='word', height=10, width=50, state='disabled')
        self.result_area.pack(pady=10)

        # Set up client socket connection
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(('127.0.0.1', 5555))  # Ensure this matches your server's address
            print("Connected to server.")
        except ConnectionRefusedError:
            messagebox.showerror("Connection Error", "Unable to connect to the server.")
            self.master.destroy()

    def prompt_word_and_send_text(self):
        """Prompt the user for the specific word before sending text."""
        self.specific_word = simpledialog.askstring("Specific Word",
                                                    "Enter the specific word to count (or type 'NONE' to skip):")
        # Start sending text in a new thread
        threading.Thread(target=self.send_text).start()

    def prompt_word_and_send_file(self):
        """Prompt the user for the specific word before sending file."""
        self.specific_word = simpledialog.askstring("Specific Word",
                                                    "Enter the specific word to count (or type 'NONE' to skip):")
        # Start sending file in a new thread
        threading.Thread(target=self.send_file).start()

    def send_text(self):
        text = self.text_area.get("1.0", tk.END).strip()
        if text:
            # Send the text data to the server
            self.client_socket.sendall(text.encode('utf-8'))
            # Send specific word to the server
            self.client_socket.sendall((self.specific_word or 'NONE').encode('utf-8'))
            self.receive_result()
        else:
            messagebox.showwarning("Warning", "Text area is empty!")

    def send_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                data = file.read()
                # Send the file data to the server
                self.client_socket.sendall(data.encode('utf-8'))
            # Send specific word to the server
            self.client_socket.sendall((self.specific_word or 'NONE').encode('utf-8'))
            self.receive_result()

    def receive_result(self):
        # Receive and display results from the server
        result = self.client_socket.recv(4096).decode('utf-8')
        self.result_area.config(state='normal')
        self.result_area.delete("1.0", tk.END)
        self.result_area.insert(tk.END, result)
        self.result_area.config(state='disabled')


# Run the client application
root = tk.Tk()
app = ClientApp(root)
root.mainloop()

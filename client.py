# client.py
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

SERVER_IP = 'roundhouse.proxy.rlwy.net' 
SERVER_PORT = 49423

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            
            msg_text = f" 💜 Friend: {data.decode()} \n"
            
            chat_area.config(state=tk.NORMAL)
            chat_area.insert(tk.END, msg_text, "friend")
            chat_area.config(state=tk.DISABLED)
            chat_area.yview(tk.END) 
        except:
            break

def send_message(event=None):
    msg = message_entry.get()
    if msg.strip() == "":
        return

    try:
        client_socket.sendall(msg.encode())
        
        msg_text = f" 🎀 You: {msg} \n"
        
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, msg_text, "you")
        chat_area.config(state=tk.DISABLED)
        chat_area.yview(tk.END)
        
        message_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", "Failed to send message.")

def connect_to_server():
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        recv_thread = threading.Thread(target=receive_messages)
        recv_thread.daemon = True
        recv_thread.start()
    except Exception as e:
        messagebox.showerror("Error", f"Could not connect to {SERVER_IP}:{SERVER_PORT}")
        root.destroy()

# --- UI SETUP ---
root = tk.Tk()
root.title("My Chat App 🌸")
root.geometry("450x600") # Made the window a little taller and wider!
root.configure(bg="#fff0f5") # Lavender Blush Background

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Helvetica", 13), bg="#fff0f5", bd=0, state=tk.DISABLED, padx=10, pady=10)
chat_area.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)

chat_area.tag_config("you", background="#ffcce6", foreground="#c2185b", justify="right", rmargin=10, lmargin1=80, lmargin2=80, spacing1=10, spacing3=10, font=("Helvetica", 12, "bold"))
chat_area.tag_config("friend", background="#e6ccff", foreground="#6a1b9a", justify="left", lmargin1=10, lmargin2=10, rmargin=80, spacing1=10, spacing3=10, font=("Helvetica", 12, "bold"))

bottom_frame = tk.Frame(root, bg="#fff0f5")
bottom_frame.pack(fill=tk.X, padx=15, pady=(0, 20))

message_entry = tk.Entry(bottom_frame, font=("Helvetica", 14), bg="white", fg="#333", relief=tk.FLAT, highlightthickness=2, highlightbackground="#ffb3c6", highlightcolor="#ff6699")
message_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15), ipady=8)
message_entry.bind("<Return>", send_message)

send_button = tk.Button(bottom_frame, text="Send 🎀", command=send_message, bg="#ff6699", fg="white", font=("Helvetica", 13, "bold"), relief=tk.FLAT, activebackground="#ff4d88", activeforeground="white")
send_button.pack(side=tk.RIGHT, ipadx=15, ipady=5)

connect_to_server()
root.mainloop()
import tkinter as tk
from tkinter import scrolledtext

def kirim_pesan():
    pesan = entry.get()
    chat_area.config(state='normal')
    chat_area.insert(tk.END, "Saya: " + pesan + "\n")
    chat_area.config(state='disabled')
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Chat Shift Malam")

chat_area = scrolledtext.ScrolledText(root, state='disabled', height=10)
chat_area.pack(padx=10, pady=10)

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

btn = tk.Button(root, text="Kirim", command=kirim_pesan)
btn.pack(pady=5)

root.mainloop()

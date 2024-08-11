import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import os
import getpass
import hashlib

class SatietyApp:
    def __init__(self, root):
        self.root = root
        self.attempts = 0
        self.password = "47c5fbf51c636da0b48309ad799e2e4d0443b9c25b055c6b762d6b6f6d95fc52"
        self.setup_ui()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self):
        hashed_input = self.hash_password(self.entry.get())
        if hashed_input == self.password:
            self.root.destroy()
        else:
            self.attempts += 1
            self.error_label.config(text=f"Code Incorrect ({self.attempts}/3)", foreground="red")
            if self.attempts >= 3:
                os.system("shutdown /s /t 1")

    def on_enter(self, event):
        event.widget.config(background="#2980b9", foreground="white")

    def on_leave(self, event):
        event.widget.config(background="#3498db", foreground="white")

    def setup_ui(self):
        self.root.title("Satiety 1.0")
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg="#2c3e50")

        frame = tk.Frame(self.root, bg="#ecf0f1", bd=5)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        label = tk.Label(frame, text="Utilisateur " + getpass.getuser(), font=("Segoe UI", 14), bg="#ecf0f1")
        label.pack(pady=10)

        self.entry = ttk.Entry(frame, show="*", font=("Segoe UI", 14))
        self.entry.pack(pady=5)

        button = tk.Button(frame, text="Valider", command=self.check_password, font=("Segoe UI", 14), bg="#3498db", fg="white", relief="flat", bd=0)
        button.pack(pady=10)
        button.bind("<Enter>", self.on_enter)
        button.bind("<Leave>", self.on_leave)

        self.error_label = tk.Label(frame, text="", font=("Segoe UI", 12), bg="#ecf0f1")
        self.error_label.pack(pady=5)

        footer_label = tk.Label(self.root, text="Satiety 1.0.0", font=("Segoe UI", 12), bg="#2c3e50", fg="white")
        footer_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

        self.root.protocol("WM_DELETE_WINDOW", lambda: None)

try:
    root = ThemedTk(theme="breeze")
    app = SatietyApp(root)
    root.mainloop()
except Exception as e:
    print(f"Erreur lors de l'initialisation de l'interface : {str(e)}")
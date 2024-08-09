import tkinter as tk
import ctypes
import os

attempts = 0

def check_code():
    global attempts
    if entry.get() == "1105":
        root.destroy()
    else:
        attempts += 1
        error_label.config(text=f"Code Incorrect ({attempts}/3)", fg="red")
        if attempts >= 3:
            os.system("shutdown /s /t 1")

root = tk.Tk()
root.title("Satiety 1.0")
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.configure(bg="#2c3e50")

frame = tk.Frame(root, bg="#ecf0f1", bd=5)
frame.place(relx=0.5, rely=0.5, anchor="center")

label = tk.Label(frame, text="Utilisateur " + os.getlogin(), font=("Helvetica", 14), bg="#ecf0f1")
label.pack(pady=10)

entry = tk.Entry(frame, show="*", font=("Helvetica", 14))
entry.pack(pady=5)

button = tk.Button(frame, text="Valider", command=check_code, font=("Helvetica", 14), bg="#3498db", fg="white")
button.pack(pady=10)

error_label = tk.Label(frame, text="", font=("Helvetica", 12), bg="#ecf0f1")
error_label.pack(pady=5)

footer_label = tk.Label(root, text="Satiety 1.0.0", font=("Helvetica", 11), bg="#2c3e50", fg="white")
footer_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

root.protocol("WM_DELETE_WINDOW", lambda: None)

root.mainloop()
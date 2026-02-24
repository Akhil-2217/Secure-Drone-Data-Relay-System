import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import os
import shutil

# ---------------- SETUP ----------------

os.makedirs("drone", exist_ok=True)

if not os.path.exists("secret.key"):
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
else:
    with open("secret.key", "rb") as f:
        key = f.read()

fernet = Fernet(key)

# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("Secure Drone-Based Data Relay System")
root.geometry("1100x700")
root.configure(bg="#e9edf2")

# ---------------- HEADER ----------------

header = tk.Label(root,
                  text="Secure Drone-Based Data Relay System",
                  bg="#3f4e6b",
                  fg="white",
                  font=("Segoe UI", 16, "bold"),
                  pady=15)
header.pack(fill="x")

title_label = tk.Label(root,
                       text="Drone Transport Simulation",
                       bg="#e9edf2",
                       font=("Segoe UI", 18, "bold"))
title_label.pack(pady=20)

# ---------------- MAIN FRAMES ----------------

main_frame = tk.Frame(root, bg="#e9edf2")
main_frame.pack(pady=10)

# -------- Network A Frame --------

frame_A = tk.LabelFrame(main_frame,
                        text="Network A - Source",
                        font=("Segoe UI", 12, "bold"),
                        padx=15, pady=15)
frame_A.grid(row=0, column=0, padx=20)

input_text = tk.Text(frame_A, width=35, height=8, font=("Segoe UI", 10))
input_text.insert("1.0", "Confidential message for transfer.")
input_text.pack(pady=10)

def encrypt_data():
    message = input_text.get("1.0", tk.END).strip()
    if not message:
        messagebox.showwarning("Warning", "Enter message!")
        return

    encrypted = fernet.encrypt(message.encode())
    with open("drone/encrypted_data.txt", "wb") as f:
        f.write(encrypted)

    update_status("✔ Data Encrypted & Loaded into Drone")

btn_encrypt = tk.Button(frame_A,
                        text="Encrypt & Load",
                        bg="#4CAF50",
                        fg="white",
                        width=20,
                        height=2,
                        command=encrypt_data)
btn_encrypt.pack(pady=10)

# -------- Drone Simulation Frame --------

frame_drone = tk.LabelFrame(main_frame,
                            text="Drone Transport Simulation",
                            font=("Segoe UI", 12, "bold"),
                            padx=15, pady=15)
frame_drone.grid(row=0, column=1, padx=20)

canvas = tk.Canvas(frame_drone, width=400, height=180, bg="white")
canvas.pack()

# Path line
canvas.create_line(50, 90, 350, 90, dash=(5, 3))

# Start & End points
canvas.create_oval(40, 80, 60, 100, fill="orange")
canvas.create_oval(340, 80, 360, 100, fill="blue")

drone_icon = canvas.create_text(50, 70, text="🚁", font=("Arial", 28))

def animate_drone():
    if not os.path.exists("drone/encrypted_data.txt"):
        messagebox.showerror("Error", "No data loaded into drone!")
        return

    shutil.copy("drone/encrypted_data.txt", "received_data.txt")

    for i in range(30):
        canvas.move(drone_icon, 10, 0)
        root.update()
        root.after(60)

    canvas.coords(drone_icon, 50, 70)
    update_status("🚁 Drone Delivered Data to Network B")

btn_transfer = tk.Button(frame_drone,
                         text="Start Drone Transfer",
                         bg="#ff8c42",
                         fg="white",
                         width=22,
                         height=2,
                         command=animate_drone)
btn_transfer.pack(pady=10)

# -------- Network B Frame --------

frame_B = tk.LabelFrame(main_frame,
                        text="Network B - Destination",
                        font=("Segoe UI", 12, "bold"),
                        padx=15, pady=15)
frame_B.grid(row=0, column=2, padx=20)

output_text = tk.Text(frame_B, width=35, height=8, font=("Segoe UI", 10))
output_text.pack(pady=10)

def decrypt_data():
    if not os.path.exists("received_data.txt"):
        messagebox.showerror("Error", "No received data!")
        return

    with open("received_data.txt", "rb") as f:
        encrypted = f.read()

    try:
        decrypted = fernet.decrypt(encrypted)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted.decode())
        update_status("✔ Data Decrypted Successfully")
    except:
        messagebox.showerror("Error", "Invalid Key!")

btn_decrypt = tk.Button(frame_B,
                        text="Decrypt Data",
                        bg="#2d6cdf",
                        fg="white",
                        width=20,
                        height=2,
                        command=decrypt_data)
btn_decrypt.pack(pady=10)

# ---------------- STATUS SECTION ----------------

status_frame = tk.Frame(root, bg="#dfe5ec", pady=20)
status_frame.pack(fill="x", pady=40)

status_label = tk.Label(status_frame,
                        text="System Ready",
                        font=("Segoe UI", 14, "bold"),
                        bg="#dfe5ec",
                        fg="#2d6cdf")
status_label.pack()

def update_status(message):
    status_label.config(text=message)

# ---------------- RUN ----------------

root.mainloop()
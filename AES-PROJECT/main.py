
import tkinter as tk

root = tk.Tk()
root.title("Ma hoa AES-128")
root.geometry("400x350")

tk.Label(root, text="MA HOA AES-128",
         font=("Arial", 18, "bold")).pack(pady=15)

tk.Label(root, text="Nhap van ban:").pack()
van_ban = tk.Entry(root, width=40)
van_ban.pack(pady=5)

tk.Label(root, text="Nhap khoa 16 ky tu:").pack()
khoa = tk.Entry(root, width=40)
khoa.pack(pady=5)

tk.Button(root, text="Ma hoa", width=15).pack(pady=5)
tk.Button(root, text="Giai ma", width=15).pack(pady=5)

tk.Label(root, text="Ket qua:").pack()
ket_qua = tk.Entry(root, width=40)
ket_qua.pack(pady=5)

root.mainloop()

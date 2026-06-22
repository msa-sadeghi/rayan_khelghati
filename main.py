import tkinter as tk

root = tk.Tk()
root.geometry("300x150")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(3, weight=1)
# بدون sticky - وسط سلول قرار می‌گیرد
tk.Label(root, text="بدون sticky", bg="lightcoral").grid(row=0, column=0, padx=5, pady=5)

# sticky="w" - به سمت چپ سلول می‌چسبد
tk.Label(root, text="sticky=w", bg="lightblue").grid(row=1, column=0, padx=5, pady=5, sticky="w")

# sticky="ew" - عرض کامل سلول را پر می‌کند
tk.Label(root, text="sticky=ew", bg="lightgreen").grid(row=2, column=0, padx=5, pady=5, sticky="ew")
tk.Label(root, text="sticky=ew", bg="lightpink").grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

root.mainloop()

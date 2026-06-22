# import tkinter as tk

# root = tk.Tk()
# root.title("کار با Pack")
# root.geometry("300x250")

# tk.Label(root, text="ردیف 1", bg="lightblue").pack(fill="x")
# tk.Label(root, text="ردیف 2", bg="lightgreen").pack(fill="x")
# tk.Label(root, text="ردیف 3", bg="lightyellow").pack(fill="x")
# tk.Label(root, text="ردیف 4", bg="red").pack(fill="x")

# root.mainloop()

import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

# بدون fill و expand
tk.Label(root, text="بدون تنظیمات", bg="lightcoral").pack()

# با fill="x" - فقط عرض را پر می‌کند
tk.Label(root, text="fill=x", bg="lightblue").pack(fill="x")

# با expand=True - فضای اضافی را اشغال می‌کند
tk.Label(root, text="expand=True", bg="lightgreen").pack(expand=True, fill="both")

root.mainloop()

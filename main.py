from tkinter import *
from tkinter import messagebox
def login():
    
    if usernameVal.get() ==  '' or passwordVal.get() == '':
        messagebox.showerror("Error", 'uername or password is empty')
        return
    if usernameVal.get() == 'admin' and passwordVal.get() == '1234':
        messagebox.showinfo("Success", "you are valid user")
    else:
        messagebox.showerror("error", "usernam or password is no correct")

window = Tk()

Label(window, text="username").grid(row=0, column=0, padx=10, pady=10)
usernameVal = StringVar()
username_entry = Entry(window, width=15,textvariable=usernameVal)
username_entry.grid(row=0, column=1, padx=10, pady=10)

Label(window, text="password").grid(row=1, column=0, padx=10, pady=10)
passwordVal = StringVar()
password_entry = Entry(window, width=15, show='*', textvariable=passwordVal)
password_entry.grid(row=1, column=1, padx=10, pady=10)

Button(window, text="Login", command=login).grid(row=2, column=0, columnspan=2, sticky="ew")
mainloop()

from tkinter import Tk, Frame, Entry, Label, Button


def login():
    print("ok")


root = Tk()


root.geometry("300x150")
root.resizable(False, False)
main_frame = Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

username_label = Label(main_frame, text="username", font=("arial", 14))
username_label.grid(row=0, column=0, sticky="w", padx=15, pady=5)
username_entry = Entry(main_frame)
username_entry.grid(row=0, column=1, sticky="w", padx=15, pady=5)

password_label = Label(main_frame, text="password", font=("arial", 14))
password_label.grid(row=1, column=0, sticky="w", padx=15, pady=5)
password_entry = Entry(main_frame)
password_entry.grid(row=1, column=1, sticky="w", padx=15, pady=5)


repassword_label = Label(main_frame, text="re-password", font=("arial", 14))
repassword_label.grid(row=2, column=0, sticky="w", padx=15, pady=5)
repassword_entry = Entry(main_frame)
repassword_entry.grid(row=2, column=1, sticky="w", padx=15, pady=5)


ok_button = Button(main_frame, text="Login", command=login)
exit_button = Button(main_frame, text="Exit", command=root.destroy)
ok_button.grid(row=3, column=0)
exit_button.grid(row=3, column=1)
root.mainloop()

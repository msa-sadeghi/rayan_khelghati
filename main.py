import tkinter as tk
from tkinter import ttk


def add_task():
    task = task_var.get().strip()
    listbox.insert(tk.END, task)


def delete_task():
    selected = listbox.curselection()
    listbox.delete(selected[0])


def save_task():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as f:
        for t in tasks:
            f.write(t + "\n")


def load_tasks():
    try:
        with open("tasks.txt") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())
    except:
        pass


app = tk.Tk()

app.geometry("400x300")

task_var = tk.StringVar()
entry = tk.Entry(app, textvariable=task_var, width=30)
entry.pack()

entry.bind("<Return>", lambda e: add_task())

listbox = tk.Listbox(app, width=40, height=10)
listbox.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

save_button = tk.Button(app, text="save Task", command=save_task)
save_button.pack(pady=5)

load_tasks()
app.mainloop()

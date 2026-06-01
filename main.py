import tkinter as tk


class TodoApp:
    def __init__(self):
        self.root = tk.Tk()

        self.app_title = "Todo App"
        self.window_width = 1000
        self.window_height = 650
        self.min_width = 900
        self.min_height = 600
        self.background_color = "#F5F7FB"
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.set_up_window()

    def set_up_window(self):
        self.root.title(self.app_title)
        self.root.configure(bg=self.background_color)
        self.root.minsize(self.min_width, self.min_height)
        self.exit_button.pack()
        self.center_window()

    def run(self):
        self.root.mainloop()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = screen_width // 2 - self.window_width // 2
        y = screen_height // 2 - self.window_height // 2
        self.root.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")
        self.root.overrideredirect(True)


app = TodoApp()
app.run()

import tkinter as tk
import configs as c
import canvas as cn
from PIL import Image, ImageTk
import os

class DisplayWindow():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = c.USED.WINDOW.WIDTH
    window_height = c.USED.WINDOW.HEIGHT
    centered = c.USED.WINDOW.CENTERED
    fullscreen = c.USED.WINDOW.FULLSCREEN
    background = c.USED.WINDOW.BACKGROUND
    title = c.USED.WINDOW.TITLE
    cursor = c.USED.WINDOW.CURSOR
    icon = c.USED.WINDOW.ICON
    version = c.USED.SOFTWARE.VERSION

    canvas_instance: cn.DisplayCanvas = None

    def __init__(self):
        self.init_window()

    def init_window(self):
        self.root.config(background=self.background)
        w, h = self.window_width, self.window_height
        if self.centered:
            center_x, center_y = int(self.screen_width / 2 - w / 2), int(self.screen_height / 2 - h / 2)
            self.root.geometry(f"{w}x{h}+{center_x}+{center_y}")
        else:
            self.root.geometry(f"{w}x{h}")
        self.root.title(self.title)
        self.root.attributes("-fullscreen", self.fullscreen)
        self.root.resizable(False, False)

        if not self.cursor:
            self.root.config(cursor="none")
        
        self.root.iconbitmap(self.icon)

        win_label = tk.Label(self.root, text=f"{self.title} - Version {self.version}", foreground="#000000", background=self.background)
        win_label.place(x=10, y=10)

        win_img = Image.open(os.path.join(c.ASSETS_FOLDER_PATH, "display_logo.png"))
        win_img_tk = ImageTk.PhotoImage(win_img)

        self.root.win_img_tk = win_img_tk

        win_img_label = tk.Label(self.root, background=self.background, image=win_img_tk)
        win_img_label.place(x=10, y=30)
    
    def attach_canvas_instance(self, canvas_instance: cn.DisplayCanvas):
        self.canvas_instance = canvas_instance
    
    def init_canvas_instance(self):
        self.canvas_instance = self.canvas_instance(self.root)

    def root_loop(self):
        self.root.mainloop()
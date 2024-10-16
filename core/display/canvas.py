import tkinter as tk
import configs as c
import window as wn
import threading as th
from PIL import Image, ImageTk

class DisplayCanvas():
    canvas_width = c.USED.CANVAS.WIDTH
    canvas_height = c.USED.CANVAS.HEIGHT
    background = c.USED.CANVAS.BACKGROUND
    delay = c.USED.CANVAS.DELAY
    fullscreen = c.USED.WINDOW.FULLSCREEN

    canvas_image = None
    canvas:tk.Canvas = None

    def __init__(self, master:tk.Tk) -> None:
        self.master = master
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        self.init_canvas(True)
    
    def resize_loop(self):
        self.canvas.config(width=self.screen_width, height=self.screen_height)
        self.master.after(100, self.resize_loop)

    def init_canvas(self, delay:bool=False):
        if delay:
            self.master.after(self.delay, self.init_canvas)
        else:
            self.canvas = tk.Canvas(self.master, width=self.screen_width, height=self.screen_height, background=self.background, highlightthickness=0)
            self.canvas.place(x=0, y=0)
            self.resize_loop_thread = th.Thread(target=self.resize_loop)
            self.resize_loop_thread.start()
    
    def show_frame(self, pil_image:Image):
        if not self.canvas:
            return
        
        if pil_image.size != (self.screen_width, self.screen_height) and self.fullscreen:
            pil_image = pil_image.resize((self.screen_width, self.screen_height))
        elif pil_image.size != (self.canvas_width, self.canvas_height):
            pil_image = pil_image.resize((self.canvas_width, self.canvas_height))
        
        tk_image = ImageTk.PhotoImage(pil_image)
        if self.canvas_image != None:
            self.canvas.itemconfig(self.canvas_image, image=tk_image)
        else:
            self.canvas_image = self.canvas.create_image(0, 0, image=tk_image, anchor="nw")
        self.canvas.image = tk_image
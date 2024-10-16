import time

__loading_frm = 0

def loading_char():
    global __loading_frm

    c = ""

    if __loading_frm == 0:
        c = "-"
    elif __loading_frm == 1:
        c = "\\"
    elif __loading_frm == 2:
        c = "|"
    elif __loading_frm == 3:
        c = "/"
        __loading_frm = -1

    __loading_frm += 1

    return c

class FPSCounter():
    def __init__(self) -> None:
        self.frames = 0
        self.fps = 0
        self.last_time = time.time()
    
    def update(self):
        if time.time() - self.last_time >= 1:
            self.fps = self.frames
            self.frames = 0
            self.last_time = time.time()
        self.frames += 1
    
    def get_fps(self) -> int:
        return self.fps
import sys
from window import *
from canvas import *
from ports import *
from listener import *
from audios import *

class Main():
    def __init__(self, argv:list[str]) -> None:
        # options = [
        #     
        # ]

        init_ports()
        
        self.display_window = DisplayWindow()

        self.display_window.attach_canvas_instance(DisplayCanvas)
        self.display_window.init_canvas_instance()

        self.display_canvas = self.display_window.canvas_instance

        self.audio_handler = AudioHandler()

        self.listener_loop_thread = listener_loop_thread(self.display_canvas.show_frame, self.audio_handler)
        
    def run(self):
        self.display_window.root_loop()

if __name__ == "__main__":
    instance = Main(sys.argv)
    instance.run()
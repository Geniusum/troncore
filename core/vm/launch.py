import sys
import configs_vm as c
import threading as th
import graphics as gr
import utils as u

sys.path.append(c.ROOT_FOLDER_PATH)
sys.path.append(c.DISPLAY_FOLDER_PATH)

import display.diffuser as df

class ConstantDiffuser():
    def __init__(self, screen_handler:gr.ScreenHandler):
        self.screen_handler: gr.ScreenHandler = screen_handler
        self.thread = th.Thread(target=self.diffuse_loop)
        # self.fps_counter = u.FPSCounter()

    def run(self):
        self.thread.start()
    
    def diffuse_loop(self):
        clear = 1
        clear_limit = 4
        while True:
            # self.fps_counter.update()
            self.screen_handler.initialize_image()
            # self.screen_handler.change_frame(self.screen_handler.hello_world(self.screen_handler.get_frame(), text=self.fps_counter.get_fps()))
            try:
                df.diffuse_image(self.screen_handler.get_frame())
            except:
                pass

            if clear == 4:
                try:
                    df.clear_old_frames()
                except:
                    pass
            
            if clear == clear_limit:
                clear = 1
            
            clear += 1

class Main():
    def __init__(self, argv:list[str]):
        self.screen_handler = gr.ScreenHandler()
        self.constant_diffuser = ConstantDiffuser(self.screen_handler)

    def run(self):
        self.constant_diffuser.run()

if __name__ == "__main__":
    instance = Main(sys.argv)
    instance.run()
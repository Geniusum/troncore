import image as im
import fluxes as fl
import configs as c
from PIL import Image
import os
import threading as th
import time

dfs_g_path = os.path.join(c.DISPLAY_FOLDER_PATH, "ports", "dfs-g.flx")

def listener_loop(show_frame_function):
    start_time = time.time()
    fps = 0
    frame = 0
    while True:
        try:
            dfs_g = fl.FluxFile(dfs_g_path)
            content = dfs_g.translate(dfs_g.try_get_content())
            print(fps)
        except fl.FluxFile.TranslationException as e:
            print(e)
        else:
            image = im.cells_to_image(content["sectors"]["PIXELS"]["cells"], content["sectors"]["INFO"]["cells"][0]["value"], content["sectors"]["INFO"]["cells"][0]["value"]) #TODO: Change size

            frame += 1

            show_frame_function(image)
            end_time = time.time()
            if end_time - start_time >= 1:
                start_time = time.time()
                fps = frame
                frame = 0

def listener_loop_thread(show_frame_function):
    thread = th.Thread(target=listener_loop, args=(show_frame_function,))
    thread.start()
    return thread
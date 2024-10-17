import image as im
import fluxes as fl
import configs as c
from PIL import Image
import os
import threading as th
import time
import audios as ad

dfs_g_path = os.path.join(c.DISPLAY_FOLDER_PATH, "ports", "dfs-g.flx")
dfs_a_path = os.path.join(c.DISPLAY_FOLDER_PATH, "ports", "dfs-a.flx")

def listener_loop(show_frame_function, audio_handler:ad.AudioHandler):
    start_time = time.time()
    fps = 0
    frame = 0
    while True:
        try:
            dfs_g = fl.FluxFile(dfs_g_path)
            content = dfs_g.translate(dfs_g.try_get_content())
        except fl.FluxFile.TranslationException as e:
            pass # print(e)
        else:
            try:
                image = Image.open(content["sectors"]["FRAME"]["cells"][0]["value"])
            except Exception as e:
                pass
            else:
                frame += 1

                show_frame_function(image)
                end_time = time.time()
                if end_time - start_time >= 1:
                    start_time = time.time()
                    fps = frame
                    frame = 0
        
        try:
            dfs_a = fl.FluxFile(dfs_a_path)
            content = dfs_a.translate(dfs_a.try_get_content())
        except fl.FluxFile.TranslationException as e:
            pass
        else:
            audio_handler.handle_sounds_sector(content["sectors"]["SOUNDS"])
            audio_handler.handle_player_sector(content["sectors"]["PLAYER"])

def listener_loop_thread(show_frame_function, audio_handler):
    thread = th.Thread(target=listener_loop, args=(show_frame_function, audio_handler))
    thread.start()
    return thread
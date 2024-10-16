import image as im
import fluxes as fl
import configs as c
from PIL import Image
import os
import time
import random
import shutil

dfs_g_path = os.path.join(c.DISPLAY_FOLDER_PATH, "ports", "dfs-g.flx")
dfs_g = fl.FluxFile(dfs_g_path)

def diffuse_image_path(image_path, divider:int=1):
    frame_path = os.path.join(c.DISPLAY_FOLDER_PATH, "ports", "data", f"{random.randint(100000, 999999)}.png")

    if divider > 1:
        image = Image.open(image_path)
        image = image.resize((int(image.size[0] / divider), int(image.size[1] / divider)))
        image.save(frame_path)
    else:
        shutil.copy(image_path, frame_path)

    content = dfs_g.translate(dfs_g.try_get_content())

    content["sectors"]["FRAME"]["cells"][0]["value"] = frame_path

    dfs_g.write_file(dfs_g_path, dfs_g.format(content))

def diffuse_image(image:Image, divider:int=1):
    frame_path = os.path.join(c.DISPLAY_FOLDER_PATH, "ports", "data", f"{random.randint(10000000, 99999999)}.png")

    if divider > 1:
        image = image.resize((int(image.size[0] / divider), int(image.size[1] / divider)))
        image.save(frame_path)
    else:
        image.save(frame_path)
        
    dfs_g.content = dfs_g.try_get_content()

    content = dfs_g.translate(dfs_g.try_get_content())

    content["sectors"]["FRAME"]["cells"][0]["value"] = frame_path

    dfs_g.write_file(dfs_g_path, dfs_g.format(content))

def clear_old_frames():
    content = dfs_g.translate(dfs_g.try_get_content())
    
    for _, __, files in os.walk(os.path.join(c.DISPLAY_FOLDER_PATH, "ports", "data")):
        for file in files:
            path = os.path.join(c.DISPLAY_FOLDER_PATH, "ports", "data", file)
            l_path = path.lower().replace("\\", "/")
            if not l_path == content["sectors"]["FRAME"]["cells"][0]["value"].lower().replace("\\", "/"):
                try:
                    os.remove(path)
                except:
                    pass


"""
i = 0

while True:
    diffuse_image_path(os.path.join(c.ASSETS_FOLDER_PATH, "test_frame.png"))
    if i == 0:
        clear_old_frames()
    
    i += 1

    if i == 4:
        i = 0"""
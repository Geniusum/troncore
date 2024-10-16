import os

DISPLAY_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
INTERN_FOLDER_PATH = os.path.join(DISPLAY_FOLDER_PATH, "intern")
ASSETS_FOLDER_PATH = os.path.join(INTERN_FOLDER_PATH, "assets")

class DEFAULT:
    class SOFTWARE:
        VERSION = "InDev 1.0"
    class CANVAS:
        WIDTH = 640
        HEIGHT = 480
        BACKGROUND = "#000000"
        DELAY = 1200
    class WINDOW:
        WIDTH = 640
        HEIGHT = 480
        FULLSCREEN = False
        CENTERED = True
        TITLE = "TronCore Display"
        BACKGROUND = "#86C6DD"
        CURSOR = False
        ICON = os.path.join(ASSETS_FOLDER_PATH, "icon.ico")

USED = DEFAULT # For debugging
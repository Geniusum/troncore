import os

VM_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
ROM_FOLDER_PATH = os.path.join(VM_FOLDER_PATH, "rom")
FONTS_FOLDER_PATH = os.path.join(VM_FOLDER_PATH, "fonts")
ROOT_FOLDER_PATH = os.path.dirname(VM_FOLDER_PATH)
DISPLAY_FOLDER_PATH = os.path.join(ROOT_FOLDER_PATH, "display")

class DEFAULT:
    class GRAPHICS:
        WIDTH = 640
        HEIGHT = 480
        BACKGROUND = "#44A0BB"

USED = DEFAULT # For debugging
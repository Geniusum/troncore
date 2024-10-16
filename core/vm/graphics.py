from PIL import Image, ImageDraw, ImageFont
import configs_vm as c
import os

class ScreenHandler():
    width = c.USED.GRAPHICS.WIDTH
    height = c.USED.GRAPHICS.HEIGHT
    background = c.USED.GRAPHICS.BACKGROUND

    def __init__(self):
        self.actual_frame: Image = Image.new("RGB", (self.width, self.height), self.background)
        self.change_frame(self.hello_world(self.actual_frame))

    def initialize_image(self):
        self.actual_frame: Image = Image.new("RGB", (self.width, self.height), self.background)
    
    def change_frame(self, new_image:Image):
        self.actual_frame = new_image
    
    def get_frame(self) -> Image:
        return self.actual_frame
    
    def hello_world(self, image:Image, color:tuple[int]=(0, 0, 0), text:str="Hello, World!") -> Image:
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(os.path.join(c.FONTS_FOLDER_PATH, "Roboto-Regular.ttf"), 32)
        text = str(text)
        draw.text((int(image.size[0] / 2), int(image.size[1] / 2)), text, color, align="center", font=font, anchor="mm")
        return image
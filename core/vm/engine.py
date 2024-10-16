# Code used by ROMs

from PIL import Image, ImageFont, ImageDraw
import fluxes as fl
import configs_vm as c
import os
import random

TTF_Font = ImageFont.truetype

class PillowStuff:
    def __init__(self) -> None:
        pass
    
    def ImageDrawInstance(self, image:Image) -> ImageDraw.Draw:
        return self.ImageDraw.Draw(image)

    def AddTextToImage(self, image:Image, *args, **kwargs):
        draw = self.self.ImageDrawInstance(image)
        draw.text(*args, **kwargs)
        return image

    def PutPixelToImage(self, image:Image, *args, **kwargs):
        image.putpixel(*args, **kwargs)
        return image

    def AddArcToImage(self, image:Image, *args, **kwargs):
        draw = self.ImageDrawInstance(image)
        draw.arc(*args, **kwargs)
        return image

    def AddChordToImage(self, image:Image, *args, **kwargs):
        draw = self.ImageDrawInstance(image)
        draw.chord(*args, **kwargs)
        return image

    def AddArcToImage(self, image:Image, *args, **kwargs):
        draw = self.ImageDrawInstance(image)
        draw.arc(*args, **kwargs)
        return image

    def AddCircleToImage(self, image:Image, *args, **kwargs):
        draw = self.ImageDrawInstance(image)
        draw.circle(*args, **kwargs)
        return image

    def AddLineToImage(self, image:Image, *args, **kwargs):
        draw = self.ImageDrawInstance(image)
        draw.line(*args, **kwargs)
        return image

    def AddPointToImage(self, image:Image, *args, **kwargs):
        draw = self.ImageDrawInstance(image)
        draw.point(*args, **kwargs)
        return image

    def AddPolygonToImage(self, image:Image, *args, **kwargs):
        draw = self.ImageDrawInstance(image)
        draw.polygon(*args, **kwargs)
        return image

    def AddRegularPolygonToImage(self, image:Image, *args, **kwargs):
        draw = self.ImageDrawInstance(image)
        draw.regular_polygon(*args, **kwargs)
        return image

    def AddRectangleToImage(self, image:Image, *args, **kwargs):
        draw = self.ImageDrawInstance(image)
        draw.rectangle(*args, **kwargs)
        return image

    def AddRounderRectangleToImage(self, image:Image, *args, **kwargs):
        draw = self.ImageDrawInstance(image)
        draw.circle(*args, **kwargs)
        return image

    def AddMultilineTextToImage(self, image:Image, *args, **kwargs):
        draw = self.ImageDrawInstance(image)
        draw.circle(*args, **kwargs)
        return image

class Audio:
    def __init__(self) -> None:
        self.dfs_a = fl.FluxFile(os.path.join(c.DISPLAY_FOLDER_PATH, "ports", "dfs-a.flx"))
    
    def GenerateSound(self, sound_path:str):
        content = self.dfs_a.try_get_content()
        keys = content["sectors"]["SOUNDS"]["cells"].keys()
        random_key = random.randint(100000000, 999999999)
        # TODO: while loop
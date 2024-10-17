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
    class FileNotFound(BaseException): ...
    class InexistantID(BaseException): ...

    def __init__(self) -> None:
        self.dfs_a_path = os.path.join(c.DISPLAY_FOLDER_PATH, "ports", "dfs-a.flx")
        self.dfs_a = fl.FluxFile(self.dfs_a_path)
    
    def GenerateSound(self, sound_path:str) -> int:
        if not os.path.exists(sound_path):
            raise self.FileNotFound(sound_path)
        content = self.dfs_a.translate(self.dfs_a.try_get_content())
        keys = list(content["sectors"]["SOUNDS"]["cells"].keys())
        random_key = random.randint(100000000, 999999999)
        while random_key in keys:
            random_key = random.randint(100000000, 999999999)
        content["sectors"]["SOUNDS"]["cells"][random_key] = {
            "type": "STRING",
            "value": sound_path
        }

        self.dfs_a.write_file(self.dfs_a_path, self.dfs_a.format(content))

        return random_key

    def PlayerCall(self, sound_id:int, action_id:int, additional_arg:int=None):
        content = self.dfs_a.translate(self.dfs_a.try_get_content())
        keys = list(content["sectors"]["SOUNDS"]["cells"].keys())
        action_id_min = 0
        action_id_max = 6
        if not sound_id in keys:
            raise self.InexistantID(sound_id)
        if max(min(action_id, action_id_max), action_id_min) != action_id:
            raise self.InexistantID(action_id)
        content["sectors"]["PLAYER"]["cells"][""]["value"] = [{
            "sector": "SOUNDS",
            "address": sound_id
        }]
        content["sectors"]["PLAYER"]["cells"][1]["value"] = action_id
        content["sectors"]["PLAYER"]["cells"][2]["value"] = True
        if additional_arg != None and isinstance(additional_arg, int):    
            content["sectors"]["PLAYER"]["cells"][3] = {
                "type": "INTEGER",
                "value": additional_arg
            }
        content["sectors"]["PLAYER"]["cells"][4] = {
            "type": "EMPTY",
            "value": None
        }
        
        self.dfs_a.write_file(self.dfs_a_path, self.dfs_a.format(content))

id = Audio().GenerateSound(r"F:\TronCore\tests\audios\test.mp3")
Audio().PlayerCall(id, 0)
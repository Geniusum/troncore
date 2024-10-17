import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

pygame.mixer.init()


#! TODO : Limiter audio channel ------------------------------------------------------------------------------------------

class AudioHandler():
    def __init__(self) -> None:
        self.channels:list[pygame.mixer.Channel] = {}
    
    def handle_sounds_sector(self, sector:dict):
        sounds = sector["cells"]
        sounds_id = list(sounds.keys())
        audios_id = list(self.channels.keys())
        if audios_id != sounds_id:
            if len(audios_id) > len(sounds_id):
                missing_id = list(set(audios_id) - set(sounds_id))
                for sound_id in missing_id:
                    del self.audios[sound_id]
            else:
                missing_id = list(set(sounds_id) - set(audios_id))
                for sound_id in missing_id:
                    if sounds[sound_id]["type"] == "STRING":
                        path = sounds[sound_id]["value"]
                        if os.path.exists(path):
                            sound = pygame.mixer.Sound(sounds[sound_id]["value"])
                            channel = pygame.mixer.Channel(0)
                            self.channels[sound_id] = [
                                sound,
                                channel,
                                False # Pause state
                            ]
        return sector
    
    def handle_player_sector(self, sector:dict):
        cells = sector["cells"]
        sound_id = cells[""]["value"][0]["address"]
        if not sound_id:
            return
        action_id = cells[1]["value"]
        to_do = cells[2]["value"]
        argument = cells[3]["value"]
        result = cells[4]["value"]
        result_type = cells[4]["type"]

        audios_id = list(self.channels.keys())

        if not sound_id in audios_id:
            return

        channel_group = self.channels[sound_id]
        
        sound:pygame.mixer.Sound = channel_group[0]
        channel:pygame.mixer.Channel = channel_group[1]
        pause_state = channel_group[2]

        if action_id == 0:
            channel.play(sound)
        elif action_id == 1:
            if pause_state:
                channel.unpause()
                pause_state = False
            else:
                channel.pause()
                pause_state = True
        elif action_id == 2:
            channel.stop()
        elif action_id == 3:
            channel.fadeout(argument)
        elif action_id == 4:
            channel.set_volume(argument)
        elif action_id == 5:
            result_type = "DECIMAL"
            result = channel.get_volume()
        elif action_id == 6:
            result_type = "BOOLEAN"
            result = channel.get_busy()
        
        if action_id in list(range(6 + 1)):
            to_do = False
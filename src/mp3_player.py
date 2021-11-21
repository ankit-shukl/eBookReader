import time
from pathlib import Path
from pygame import mixer

class mp3_player:
    def __init__(self) -> None:
        self.is_playing = False
        self.player = None

    def play(self, mp3_file_path:str) -> None:
        if self.is_playing == False:
            while Path(mp3_file_path).is_file() is False:            
                print("waiting for audio file to be created", end='')
                time.sleep(1)
                print('.', end='')
            mixer.init()
            mixer.music.load(mp3_file_path)
            mixer.music.play()
            self.is_playing = True

    def stop_playing(self) -> None:
        if self.is_playing == True:
            self.is_playing = False
            mixer.music.stop() 

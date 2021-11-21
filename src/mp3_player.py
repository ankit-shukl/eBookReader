import time
from pathlib import Path
from pygame import mixer

class mp3_player:
    def __init__(self) -> None:
        self.is_playing = False
        self.player = None

    def play(self, mp3_file_path:str) -> None:
        b_message_printed=False
        if not self.is_playing:
            while Path(mp3_file_path).is_file() is False:
                if b_message_printed is False:
                    print("Waiting for audio file to be created", end='')
                    b_message_printed = True
                else:
                    print(".", end='')
                time.sleep(5)
            mixer.init()
            mixer.music.load(mp3_file_path)
            mixer.music.play()
            self.is_playing = True

    def stop_playing(self) -> None:
        if self.is_playing:
            self.is_playing = False
            mixer.music.stop() 

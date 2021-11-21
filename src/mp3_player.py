from pathlib import Path
import time
import multiprocessing
from gtts import gTTS
from playsound import playsound

class mp3_player:
    def __init__(self) -> None:
        self.is_playing = False
        self.player = None

    def __del__(self):
        self.stop_playing()
        pass

    def play(self, mp3_file_path:str) -> None:
        if self.is_playing == False:
            while Path(mp3_file_path).is_file() is False:            
                print("waiting for audio file to be created", end='')
                time.sleep(1)
                print('.', end='')
            self.player = multiprocessing.Process(target=playsound, args=(mp3_file_path,))
            self.player.start()
            self.is_playing = True

    def stop_playing(self) -> None:
        print('stopping playing')
        if self.is_playing:
            self.player.terminate()
            self.player.join()
            self.player = None
            self.is_playing = False

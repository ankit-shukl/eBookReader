from pathlib import Path
import time
import multiprocessing
from gtts import gTTS
from playsound import playsound

class mp3_manager:
    def __init__(self) -> None:
        self.is_writing = False        
        self.writer = None
        self.playing = False
        self.player = None
        self.mp3_dir_path = None

    def __del__(self):
        self.stop_writing()
        self.stop_playing()
        pass

    def set_dir_path(self, dir_path: str) -> None:
        self.mp3_dir_path = dir_path

    def get_mp3_file_path(self, page_no: int) -> str:
        return self.mp3_dir_path + '/' + str(page_no) + '.mp3'

    def write(self, text: str, page_no : int) -> None:
        if self.mp3_dir_path is None:
            return
        mp3_file_path = self.get_mp3_file_path(page_no)
        if Path(mp3_file_path).is_file():
            return

        if self.is_writing is False:
            self.is_writing = True
            gTTS(text=text).save(mp3_file_path)
            # self.writer = multiprocessing.Process(target=gTTS-cli, args=(text, "--output", file_path)).start()
            # await asyncio.sleep(2)

    def stop_writing(self) -> None:
        # if self.is_writing is True:
        #    self.writer.terminate()
        #    self.is_writing = False
        pass
        
    def play(self, page_no: int) -> None:
        if self.mp3_dir_path is None:
            return
        mp3_file_path = self.get_mp3_file_path(page_no)
        if self.playing == False:
            while Path(mp3_file_path).is_file() is False:            
                print("waiting for audio file to be created", end='')
                time.sleep(1)
                print('.', end='')
            self.player = multiprocessing.Process(target=playsound, args=(mp3_file_path,))
            self.player.start()
            self.playing = True

    def stop_playing(self) -> None:
        print('stopping playing')
        if self.playing:
            self.player.terminate()
            self.player.join()
            self.player = None
            self.playing = False

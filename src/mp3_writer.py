from pathlib import Path
import time
import multiprocessing
from gtts import gTTS

class mp3_writer:
    def __init__(self) -> None:
        self.is_writing = False        
        self.writer = None
        self.mp3_dir_path = None

    def __del__(self):
        self.stop_writing()
        pass

    def set_dir_path(self, dir_path: str) -> None:
        self.mp3_dir_path = dir_path

    def get_mp3_file_path(self, page_no: int) -> str:
        return self.mp3_dir_path + '/' + str(page_no) + '.mp3'

    def write(self, text: str, mp3_file_path : str) -> None:
        if Path(mp3_file_path).is_file():
            return
        if self.is_writing is False:
            self.is_writing = True
            gTTS(text=text).save(mp3_file_path)

    def stop_writing(self) -> None:
        pass

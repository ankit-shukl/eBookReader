from pathlib import Path
from gtts import gTTS

class mp3_writer:
    def __init__(self) -> None:
        self.writer = None
        self.mp3_dir_path = None

    def set_dir_path(self, dir_path: str) -> None:
        self.mp3_dir_path = dir_path

    def get_mp3_file_path(self, page_no: int) -> str:
        return self.mp3_dir_path + '/' + str(page_no) + '.mp3'

    def write(self, text: str, mp3_file_path : str):
        if Path(mp3_file_path).is_file():
            return
        gTTS(text=text).save(mp3_file_path)

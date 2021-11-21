from pathlib import Path
from mp3_writer import mp3_writer
from mp3_player import mp3_player

class mp3_manager:
    def __init__(self) -> None:
        self.writer = mp3_writer()
        self.player = mp3_player()
        self.mp3_dir_path = None

    def __del__(self):
        self.writer.stop_writing()
        self.player.stop_playing()
        pass

    def set_dir_path(self, dir_path: str) -> None:
        self.mp3_dir_path = dir_path

    def get_mp3_file_path(self, page_no: int) -> str:
        return self.mp3_dir_path + '/' + str(page_no) + '.mp3'

    def write(self, text: str, page_no : int) -> None:
        if self.mp3_dir_path is None:
            raise Exception('Audio file directory path is None') 
        mp3_file_path = self.get_mp3_file_path(page_no)
        self.writer.write(text, mp3_file_path)

    def stop_writing(self) -> None:
        self.writer.stop_writing()
        
    def play(self, page_no: int) -> None:
        if self.mp3_dir_path is None:
            return
        mp3_file_path = self.get_mp3_file_path(page_no)
        self.player.play(mp3_file_path)

    def stop_playing(self) -> None:
        self.player.stop_playing()
        
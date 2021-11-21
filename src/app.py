import os
from viewer import Viewer
from pdf_manager import pdf_manager
from mp3_manager import mp3_manager

class App:
    def __init__(self):
        self.pdf_manager = pdf_manager()
        self.audio_manager = mp3_manager()
        self.viewer = Viewer(self.pdf_manager, self.audio_manager)
        
    def __del__(self):
        self.pdf_manager.__del__()
        self.audio_manager.__del__()
        self.viewer.__del__()
        
    def run(self):
        self.viewer.show_page()
        

def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()

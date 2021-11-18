import os
from tkinter import *
from tkinter import ttk
from mp3_manager import mp3_manager
from pdf_reader import PDFReader
from pathlib import Path
# import asyncio
from tkinter import filedialog

class Viewer:
    def __init__(self, pdf_reader=None, audio_manager=None):
        self.pdf_reader = pdf_reader
        self.audio_manager = audio_manager
        self.page_no = 1
        self.init_ui()
        self.frm = ttk.Frame(self.root, padding=10)
        self.pdf_file_path = None

    def __del__(self):
        self.root.destroy()
        
    def init_ui(self):
        self.root = Tk()
        self.root.title("My Audible")
        self.root.geometry("650x450+700+200")

    def show_page(self): 
        self.frm.grid()
        ttk.Button(self.frm, text ="Browse", command=self.browse_file).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(self.frm, text="Previous", command=self.prev_page).grid(row=0, column=1, padx=10, pady=10)
        if self.pdf_file_path is not None and Path(self.pdf_file_path).is_file():
            ttk.Label(self.frm, width=30, text="Page# " + str(self.page_no) + " / " + str(self.pdf_reader.page_count)).grid(row=0, column=2, padx=10, pady=10)
        else:
            ttk.Label(self.frm, width=30, text="Click Browse and select PDF file").grid(row=0, column=2, padx=10, pady=10)
        ttk.Button(self.frm, text="Next", command=self.next_page).grid(row=0, column=3, padx=10, pady=10)
        if self.pdf_file_path is not None and Path(self.pdf_file_path).is_file():
            page_text = self.pdf_reader.read_page(self.page_no)
            if page_text is not None and len(page_text) > 0:
                self.audio_manager.write(page_text, self.page_no)
                self.audio_manager.play(self.page_no)
                ttk.Label(self.frm, text=page_text).grid( row=1, padx= 100, pady=50)
        self.root.mainloop()

    def browse_file(self):
        self.pdf_file_path = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
        self.pdf_reader.set_file_path(self.pdf_file_path)
        audio_dir_path = self.pdf_file_path[:self.pdf_file_path.rfind('/')] + '/' + self.pdf_file_path.split('/')[-1].split('.')[0]
        if os.path.isdir(audio_dir_path) is False:
            print('Creating audio file directory : ' + audio_dir_path)
            os.mkdir(audio_dir_path)
        self.audio_manager.set_dir_path(audio_dir_path)
        self.show_page()

    def next_page(self):
        if self.pdf_file_path is not None and Path(self.pdf_file_path).is_file():
            self.audio_manager.stop_playing()
            self.page_no += 1
            self.show_page()

    def prev_page(self):
        if self.pdf_file_path is not None and Path(self.pdf_file_path).is_file():
            self.audio_manager.stop_playing()
            self.page_no -= 1
            self.show_page()
    

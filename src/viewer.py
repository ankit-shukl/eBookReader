import os
from tkinter import *
from tkinter import ttk
from mp3_manager import mp3_manager
from pdf_manager import pdf_manager
from pathlib import Path
# import asyncio
from tkinter import filedialog
import threading
import time

class Viewer:
    def __init__(self, pdf_manager=None, audio_manager=None):
        self.pdf_manager = pdf_manager
        self.audio_manager = audio_manager
        self.page_no = 1
        self.pdf_file_path = None
        self.init_ui()

    def __del__(self):
        self.root.destroy()
        
    def init_ui(self):
        self.root = Tk()
        self.root.title("My Audible")
        self.root.geometry("650x450+700+200")
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        ttk.Button(self.frm, text ="Browse", command=self.browse_file).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(self.frm, text="Previous", command=self.prev_page).grid(row=0, column=1, padx=10, pady=10)
        self.labltext_page_no=StringVar(master=self.frm, value="Click Browse and select PDF file")
        ttk.Label(self.frm, width=30, textvariable=self.labltext_page_no).grid(row=0, column=2, padx=10, pady=10)
        ttk.Button(self.frm, text="Next", command=self.next_page).grid(row=0, column=3, padx=10, pady=10)
        #ttk.Button(self.frm, text="Exit", command=self.__del__()).grid(row=0, column=4, padx=10, pady=10)
        self.labltext_page_content=StringVar(master=self.frm, value="")
        ttk.Label(self.frm, textvariable=self.labltext_page_content).grid( row=1, padx= 100, pady=50)

    def show_page(self): 
        if self.pdf_file_path is not None and Path(self.pdf_file_path).is_file():
            self.labltext_page_no.set("Page# " + str(self.page_no) + " / " + str(self.pdf_manager.get_page_count()))
            page_text = self.pdf_manager.read_page(self.page_no)
            if page_text is not None:                
                self.labltext_page_content.set(page_text)
                if self.page_no % 4 == 1:
                    if not Path(self.audio_manager.get_dir_path() + "/" + str(self.page_no+3) + ".mp3").is_file():
                        t_list = []
                        start = time.time()
                        for i in range(4):
                            w = mp3_manager()
                            w.set_dir_path(self.audio_manager.get_dir_path())
                            t = threading.Thread(target=self.audio_manager.write(self.pdf_manager.read_page(self.page_no + i), self.page_no + i))
                            t_list.append(t)
                            print("thread_" + str(self.page_no + i) + " created. t=" + str(time.time() - start))
                        for i in range(4):
                            print("thread_" + str(self.page_no + i) + " started. t=" + str(time.time() - start))
                            t_list[i].start()
                        for i in range(4):
                            print("thread_" + str(self.page_no + i) + " joined. t=" + str(time.time() - start))
                            t_list[i].join()
                        time.sleep(20)
                    t_list_2 = []
                    for i in range(4):
                        w = mp3_manager()
                        w.set_dir_path(self.audio_manager.get_dir_path())
                        t = threading.Thread(
                            target=self.audio_manager.write(self.pdf_manager.read_page(self.page_no + 4 + i),
                                                            self.page_no + 4 + i))
                        t_list_2.append(t)
                        print("thread_" + str(self.page_no + 4 + i) + " created. t=" + str(time.time() - start))
                    for i in range(4):
                        print("thread_" + str(self.page_no + 4 + i) + " started. t=" + str(time.time() - start))
                        t_list_2[i].start()
                    for i in range(4):
                        print("thread_" + str(self.page_no + 4 + i) + " joined. t=" + str(time.time() - start))
                        t_list_2[i].join()
                    #time.sleep(60)
                    # t_list_3 = []
                    # for i in range(4):
                    #     w = mp3_manager()
                    #     w.set_dir_path(self.audio_manager.get_dir_path())
                    #     t = threading.Thread(target=self.audio_manager.write(self.pdf_manager.read_page(self.page_no + 8 + i), self.page_no + 8 + i))
                    #     t_list_3.append(t)
                    #     print("thread_" + str(self.page_no + 8 + i) + " created. t=" + str(time.time() - start))
                    # for i in range(4):
                    #     print("thread_" + str(self.page_no + 8 + i) + " started. t=" + str(time.time() - start))
                    #     t_list_3[i].start()
                    # for i in range(4):
                    #     print("thread_" + str(self.page_no + 8 + i) + " joined. t=" + str(time.time() - start))
                    #     t_list_3[i].join()
                    # time.sleep(90)
                    # t_list_4 = []
                    # for i in range(4):
                    #     w = mp3_manager()
                    #     w.set_dir_path(self.audio_manager.get_dir_path())
                    #     t = threading.Thread(target=self.audio_manager.write(self.pdf_manager.read_page(self.page_no + 12 + i), self.page_no + 12 + i))
                    #     t_list_4.append(t)
                    #     print("thread_" + str(self.page_no + 12 + i) + " created. t=" + str(time.time() - start))
                    # for i in range(4):
                    #     print("thread_" + str(self.page_no + 12 + i) + " started. t=" + str(time.time() - start))
                    #     t_list_4[i].start()
                    # for i in range(4):
                    #     print("thread_" + str(self.page_no + 12 + i) + " joined. t=" + str(time.time() - start))
                    #     t_list_4[i].join()
                self.audio_manager.play(self.page_no)
        self.root.mainloop()

    def browse_file(self):
        self.pdf_file_path = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
        self.pdf_manager.set_file_reader(self.pdf_file_path)
        audio_dir_path = self.pdf_file_path[:self.pdf_file_path.rfind('/')] + '/' + self.pdf_file_path.split('/')[-1].split('.')[0]
        if not os.path.isdir(audio_dir_path):
            print('Creating audio file directory : ' + audio_dir_path)
            os.mkdir(audio_dir_path)
        self.audio_manager.set_dir_path(audio_dir_path)
        self.show_page()

    def next_page(self):
        if self.pdf_file_path is not None and Path(self.pdf_file_path).is_file():
            self.audio_manager.stop_playing()
            if self.page_no < self.pdf_manager.get_page_count():
                self.page_no += 1
                self.show_page()

    def prev_page(self):
        if self.pdf_file_path is not None and Path(self.pdf_file_path).is_file():
            self.audio_manager.stop_playing()
            if self.page_no > 1:
                self.page_no -= 1
                self.show_page()
 
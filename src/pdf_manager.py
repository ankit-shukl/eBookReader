from pdf_reader_PyPDF2 import pdf_reader_PyPDF2
from pdf_reader_pdfPlumber import pdf_reader_pdfPlumber

class pdf_manager:
    def __init__(self) -> None:
        self.file_reader = pdf_reader_pdfPlumber()

    def set_file_reader(self, file_path):
        self.file_reader.set_file_reader(file_path)

    def get_page_count(self):
        self.file_reader.get_page_count()

    def read_page(self, page_no):
        if self.file_reader is None:
            raise Exception("No file set")
        else:            
            return self.file_reader.read_page(page_no)

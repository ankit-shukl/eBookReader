import PyPDF2

class pdf_reader_PyPDF2:
    def __init__(self) -> None:
        self.file_reader = None

    def set_file_reader(self, file_path):
        self.file_reader = PyPDF2.PdfFileReader(open(file_path, 'rb'))
                
    def get_page_count(self):
        return self.file_reader.getNumPages()
        
    def read_page(self, page_no):
        page = self.file_reader.getPage(page_no)
        return page.extractText()

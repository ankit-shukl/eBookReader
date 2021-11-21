#import PyPDF2
import pdfplumber

class PDFReader:
    def __init__(self) -> None:
        self.file_reader = None
        self.page_count = None

    def __del__(self):
        pass

    def set_file_path(self, file_path):
        #self.file_reader = PyPDF2.PdfFileReader(open(file_path, 'rb'))      
        self.file_reader = pdfplumber.open(file_path)
        self.page_count = self.get_page_count()
        
    def get_page_count(self):
        #return self.file_reader.getNumPages()
        return len(self.file_reader.pages)

    def read_page(self, page_no):
        # if self.file_reader is None:
        #     raise Exception("No file set")
        # else:
        #     page = self.file_reader.getPage(page_no)
        #     return page.extractText()
        if self.file_reader is None:
            raise Exception("No file set")
        else:
            page = self.file_reader.pages[page_no]
            return page.extract_text()



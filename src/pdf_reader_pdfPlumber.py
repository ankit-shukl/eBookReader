import pdfplumber

class pdf_reader_pdfPlumber:
    def __init__(self) -> None:
        self.file_reader = None

    def set_file_reader(self, file_path):
        self.file_reader = pdfplumber.open(file_path)
        
    def get_page_count(self):
        return len(self.file_reader.pages)

    def read_page(self, page_no):
        page = self.file_reader.pages[page_no]
        return page.extract_text()
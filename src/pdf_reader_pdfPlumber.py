import pdfplumber

class pdf_reader_pdfPlumber:
    def __init__(self) -> None:
        self.file_reader = None

    def set_file_reader(self, file_path) -> None:
        self.file_reader = pdfplumber.open(file_path)
        
    def get_page_count(self) -> int:
        l = len(self.file_reader.pages)
        return l

    def read_page(self, page_no) -> str:
        page = self.file_reader.pages[page_no]
        return page.extract_text()
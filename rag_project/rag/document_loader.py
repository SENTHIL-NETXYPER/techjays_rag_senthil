from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

import fitz
def read_pdf(file_path):
             
             reader=PdfReader(file_path)
             doc=fitz.open(file_path)
             text=""
             for page in doc:
                     text += page.get_text()
             return text        


def clean_text(text):
        text=text.replace(" ","")
        #for cleaning remving sapces between individual char 
        return text

def chunk_text(text):
        splitter=RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50
        )
        chunks= splitter.split_text(text)
        return chunks
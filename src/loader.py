
from langchain_community.document_loaders import UnstructuredPDFLoader

import re

class PDFLoader:
    def __init__(self, pdf_path: str):
        self.pdf_path=pdf_path
        
    def load_pdf(self):
        print("="*50)
        print("Loading PDF...")
        print("="*50)
        
        loader=UnstructuredPDFLoader(self.pdf_path, mode="paged", strategy="fast")
        documents=loader.load()
        print(f"\nTotal Pages loaded : {len(documents)}")
        
        return documents
    def add_metadata(self, documents):
        print("\nAdding metadata..")
        for i, doc in enumerate(documents,1):
            text=doc.page_content.strip()
            if "page_number" in doc.metadata:
                doc.metadata["page"] = doc.metadata["page_number"]
            else:
                doc.metadata["page"] = i + 1

            doc.metadata["document_name"] = self.pdf_path.split("/")[-1]
            
            doc.metadata["source"]=self.pdf_path
            
            lines = text.split("\n")
            def detect_heading(text):
                for line in lines[:5]:
                    line = line.strip()

                    if not line:
                        continue

                    
                    if len(line) < 100:

                        # Numbered section
                        if re.match(r"^\d+(\.\d+)*", line):
                            return line

                        # Title Case heading
                        if line.istitle():
                            return line

                        # ALL CAPS heading
                        if line.isupper():
                            return line

                        # Ends with colon
                        if line.endswith(":"):
                            return line

                return "Unknown"
            doc.metadata["heading"] = detect_heading(doc.page_content)
            
            if "|" in text:
                content_type='table'
            elif len(lines)>5:
                content_type='text'
            else:
                content_type='short_text'
                
            doc.metadata['content_type']=content_type
            doc.metadata['length']=len(text)
            
        print("Metadata Added Successfully!")      
        return documents
 
    def preview(self, documents, pages=2):
        print("\nPreview : ")
        print("="*50)
        
        for doc in documents[:pages]:
            print("Metadata Information - ")
            print(f"\nPage : {doc.metadata['page']}")
            print(f"\nSource Path : {doc.metadata['source']}")
            print(f"\nHeading : {doc.metadata['heading']}")
            print(f"\nContent Type : {doc.metadata['content_type']}")
            print(f"\nlength : {doc.metadata['length']}")
            print("-"*50)
            
            print(doc.page_content)
            print('\n')
    
    def load(self):
        documents=self.load_pdf()
        documents=self.add_metadata(documents)
        self.preview(documents)
        
        return documents
        
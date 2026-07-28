from langchain_experimental.text_splitter import SemanticChunker
import re

class SemanticChunkerService:
    def __init__(self, embeddings):
        self.chunker = SemanticChunker(embeddings=embeddings)

    def create_chunks(self, documents):
        
        chunks = self.chunker.split_documents(documents)

        for i, chunk in enumerate(chunks,1):
            text = chunk.page_content.strip()
            lines = [line.strip() for line in text.split("\n") if line.strip()]

            if "page_number" in chunk.metadata:
                chunk.metadata["page"] = chunk.metadata["page_number"]
            else:
                chunk.metadata["page"] = i + 1
                
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
            
            if "|" in text:
                content_type = "table"
            elif len(lines) > 5:
                content_type = "text"
            else:
                content_type = "short_text"
            
            chunk.metadata["heading"] = detect_heading(chunk.page_content)
            chunk.metadata["content_type"] = content_type
            chunk.metadata["length"] = len(text)

        print(f"\nTotal Chunks after Semantic Chunker : {len(chunks)}")

        return chunks
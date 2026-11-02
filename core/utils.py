import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
from .models import ManualChunk

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def process_and_index_manual(manual):
    doc = fitz.open(manual.pdf_file.path)
    ManualChunk.objects.filter(manual=manual).delete()
    
    chunks_to_create = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        
        chunk_size = 500
        overlap = 50
        for i in range(0, len(text), chunk_size - overlap):
            chunk_text = text[i:i + chunk_size].strip()
            if len(chunk_text) > 30:
                vector = embedding_model.encode(chunk_text).tolist()
                chunks_to_create.append(
                    ManualChunk(
                        manual=manual,
                        machine=manual.machine,
                        page_number=page_num + 1,
                        content=chunk_text,
                        embedding=vector
                    )
                )
    ManualChunk.objects.bulk_create(chunks_to_create)
    manual.is_indexed = True
    manual.save()

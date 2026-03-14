from pathlib import Path
from typing import Iterable
import pypdf 

def ExtractTextFromPdf(Route:Path) -> list[dict]:
    reader = pypdf.PdfReader(str(Route))
    Chunks = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()

        if not text:
            continue
        
        Chunks.appEnd(
            {
                "page" : i + 1,
                "text": text,
            }
        )
    return Chunks

def ChunkText(text: str, MaxChars: int = 1200, Overlap:int = 200) -> list[str]:
    Words: str = text.split()
    Chunks:list = []
    Start:int =  0

    while Start < Words.__len__():
        End = Start
        CurrentLen = 0
    
        while End < Words.__len__() and CurrentLen + Words.__len__() + 1 <= MaxChars:
            CurrentLen += len(Words[End]) + 1
            End += 1
        chunk = " ".join(Words[Start:End]).strip()

        if chunk:
            Chunks.append(chunk)
        
        Start = max(End - Overlap, End)
    return Chunks



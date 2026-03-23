import json
import time
from io import BytesIO

import pypdfium2 as pdfium

from app.service.documents import DocumentService

if __name__ == "__main__":
    svc = DocumentService()

    with open("data/pdfs/paper9111.pdf", "rb") as f:
        pdf_bytes = f.read()

    pdf = pdfium.PdfDocument(BytesIO(pdf_bytes))
    num_pages = len(pdf)
    pdf.close()
    print(f"Document: paper9111.pdf ({num_pages} pages)\n")

    outputs = {
        "md": ("paper9111.md", svc.convert_to_md),
        "json": ("paper9111.json", svc.convert_to_json),
        "html": ("paper9111.html", svc.convert_to_html),
        "text": ("paper9111.txt", svc.convert_to_text),
        "doctags": ("paper9111.doctags.txt", svc.convert_to_doctags),
    }

    for fmt, (filename, method) in outputs.items():
        print(f"Converting to {fmt}...")
        start = time.perf_counter()
        result = method("paper9111.pdf", BytesIO(pdf_bytes))
        elapsed = time.perf_counter() - start
        per_page = elapsed / num_pages

        path = f"data/outputs/{filename}"
        if isinstance(result, dict):
            with open(path, "w") as f:
                json.dump(result, f, indent=2)
        else:
            with open(path, "w") as f:
                f.write(str(result))

        print(f"  Saved {path}")
        print(f"  {elapsed:.2f}s total | {per_page:.2f}s per page\n")

    print("Done!")
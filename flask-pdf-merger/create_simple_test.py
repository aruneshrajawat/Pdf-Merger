#!/usr/bin/env python3
"""
Create a simple test PDF for download testing
"""
from PyPDF2 import PdfWriter
import os

def create_test_pdf():
    # Create a simple test PDF
    writer = PdfWriter()
    
    # Add a blank page (minimal PDF)
    from PyPDF2.generic import PageObject
    from PyPDF2.generic import RectangleObject
    
    page = PageObject.create_blank_page(width=612, height=792)  # Letter size
    writer.add_page(page)
    
    # Save to output folder
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    filename = 'test_merged.pdf'
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'wb') as f:
        writer.write(f)
    
    print(f"✅ Created test PDF: {filepath}")
    print(f"File size: {os.path.getsize(filepath)} bytes")
    print(f"Download URL: http://localhost:5000/download_file/{filename}")

if __name__ == "__main__":
    create_test_pdf()
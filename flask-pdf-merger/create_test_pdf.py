#!/usr/bin/env python3
"""
Create test PDF files for testing the merger
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

def create_test_pdf(filename, content):
    """Create a simple test PDF"""
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Add some content
    c.drawString(100, height - 100, f"Test PDF: {content}")
    c.drawString(100, height - 150, "This is a test document for PDF merger.")
    c.drawString(100, height - 200, f"Filename: {filename}")
    
    # Add a second page
    c.showPage()
    c.drawString(100, height - 100, f"Page 2 of {content}")
    c.drawString(100, height - 150, "Second page content")
    
    c.save()
    print(f"Created: {filename}")

if __name__ == "__main__":
    # Create test directory
    os.makedirs('test_pdfs', exist_ok=True)
    
    # Create test PDFs
    create_test_pdf('test_pdfs/document1.pdf', 'Document 1')
    create_test_pdf('test_pdfs/document2.pdf', 'Document 2')
    create_test_pdf('test_pdfs/document3.pdf', 'Document 3')
    
    print("Test PDFs created in test_pdfs/ directory")
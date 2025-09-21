#!/usr/bin/env python3
"""
Simple test to create sample PDFs and test upload
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

def create_sample_pdfs():
    """Create sample PDF files for testing"""
    os.makedirs('sample_pdfs', exist_ok=True)
    
    # Create PDF 1
    c1 = canvas.Canvas('sample_pdfs/sample1.pdf', pagesize=letter)
    c1.drawString(100, 750, "Sample PDF Document 1")
    c1.drawString(100, 700, "This is the first test document.")
    c1.drawString(100, 650, "It has some sample content for testing.")
    c1.save()
    
    # Create PDF 2
    c2 = canvas.Canvas('sample_pdfs/sample2.pdf', pagesize=letter)
    c2.drawString(100, 750, "Sample PDF Document 2")
    c2.drawString(100, 700, "This is the second test document.")
    c2.drawString(100, 650, "It also has sample content for testing.")
    c2.save()
    
    print("✅ Created sample PDFs:")
    print("   - sample_pdfs/sample1.pdf")
    print("   - sample_pdfs/sample2.pdf")
    print("\n📋 To test:")
    print("   1. Start the server: python3 debug_session.py")
    print("   2. Go to http://localhost:5000")
    print("   3. Upload the sample PDFs from sample_pdfs/ folder")
    print("   4. Check debug info at http://localhost:5000/debug")

if __name__ == "__main__":
    create_sample_pdfs()
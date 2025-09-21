#!/usr/bin/env python3
"""
Test the complete PDF merger flow
"""

import os
import tempfile
from io import BytesIO
from app import app
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_test_pdf_content(title):
    """Create a simple PDF in memory"""
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    c.drawString(100, height - 100, f"Test PDF: {title}")
    c.drawString(100, height - 150, "This is a test document.")
    c.save()
    
    buffer.seek(0)
    return buffer

def test_complete_flow():
    """Test the complete upload -> merge -> download flow"""
    with app.test_client() as client:
        with client.session_transaction() as sess:
            # Clear any existing session
            sess.clear()
        
        print("1. Testing home page...")
        response = client.get('/')
        assert response.status_code == 200
        print("   ✓ Home page loads")
        
        print("2. Testing file upload...")
        
        # Create test PDF files
        pdf1 = create_test_pdf_content("Document 1")
        pdf2 = create_test_pdf_content("Document 2")
        
        # Simulate file upload
        data = {
            'files': [
                (pdf1, 'test1.pdf'),
                (pdf2, 'test2.pdf')
            ],
            'merge_order': 'filename',
            'output_name': 'test_merged.pdf'
        }
        
        response = client.post('/upload', data=data, content_type='multipart/form-data')
        print(f"   Upload response: {response.status_code}")
        
        if response.status_code == 302:  # Redirect to merge page
            print("   ✓ Upload successful, redirected to merge page")
            
            print("3. Testing merge page...")
            response = client.get('/merge')
            print(f"   Merge page response: {response.status_code}")
            
            if response.status_code == 200:
                print("   ✓ Merge page loads")
                
                print("4. Testing PDF merge process...")
                merge_data = {
                    'output_filename': 'test_merged.pdf',
                    'add_bookmarks': 'on'
                }
                
                response = client.post('/process', data=merge_data)
                print(f"   Process response: {response.status_code}")
                
                if response.status_code == 302:  # Redirect to download page
                    print("   ✓ Merge successful, redirected to download page")
                    
                    print("5. Testing download page...")
                    response = client.get('/download/test_merged.pdf')
                    print(f"   Download page response: {response.status_code}")
                    
                    if response.status_code == 200:
                        print("   ✓ Download page loads")
                        print("   ✓ Download button should be visible!")
                        
                        # Check if the download file endpoint works
                        print("6. Testing file download...")
                        response = client.get('/download_file/test_merged.pdf')
                        print(f"   File download response: {response.status_code}")
                        
                        if response.status_code == 200:
                            print("   ✓ File download works!")
                            print("   ✓ Complete flow successful!")
                            return True
                        else:
                            print(f"   ✗ File download failed: {response.status_code}")
                    else:
                        print(f"   ✗ Download page failed: {response.status_code}")
                else:
                    print(f"   ✗ Merge failed: {response.status_code}")
            else:
                print(f"   ✗ Merge page failed: {response.status_code}")
        else:
            print(f"   ✗ Upload failed: {response.status_code}")
    
    return False

if __name__ == "__main__":
    print("Testing complete PDF merger flow...")
    print("=" * 50)
    
    try:
        success = test_complete_flow()
        if success:
            print("\n🎉 All tests passed! The download button should work.")
        else:
            print("\n❌ Some tests failed. Check the output above.")
    except Exception as e:
        print(f"\n💥 Test failed with error: {e}")
        import traceback
        traceback.print_exc()
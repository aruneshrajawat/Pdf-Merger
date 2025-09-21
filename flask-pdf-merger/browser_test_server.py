#!/usr/bin/env python3
"""
Browser-compatible test server for download testing
"""

from app import app
from flask import Response
import os

@app.route('/test_browser_download/<filename>')
def test_browser_download(filename):
    """Browser-compatible download with multiple fallbacks"""
    try:
        file_path = os.path.abspath(os.path.join(app.config['OUTPUT_FOLDER'], filename))
        
        if not os.path.exists(file_path):
            return f"File not found: {filename}", 404
        
        # Read file content
        with open(file_path, 'rb') as f:
            file_data = f.read()
        
        # Create response with explicit headers for browser compatibility
        response = Response(
            file_data,
            mimetype='application/pdf',
            headers={
                'Content-Disposition': f'attachment; filename="{filename}"',
                'Content-Type': 'application/pdf',
                'Content-Length': str(len(file_data)),
                'Cache-Control': 'no-cache, no-store, must-revalidate',
                'Pragma': 'no-cache',
                'Expires': '0'
            }
        )
        
        print(f"DEBUG: Serving {filename} ({len(file_data)} bytes)")
        return response
        
    except Exception as e:
        print(f"DEBUG: Browser download failed: {str(e)}")
        return f"Download failed: {str(e)}", 500

@app.route('/test_page')
def test_page():
    """Simple test page with download links"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Download Test</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .btn { 
                display: inline-block; 
                padding: 10px 20px; 
                margin: 10px; 
                background: #007bff; 
                color: white; 
                text-decoration: none; 
                border-radius: 5px; 
            }
            .btn:hover { background: #0056b3; }
            .test-section { 
                border: 1px solid #ddd; 
                padding: 20px; 
                margin: 20px 0; 
                border-radius: 5px; 
            }
        </style>
    </head>
    <body>
        <h1>🧪 PDF Download Test Page</h1>
        
        <div class="test-section">
            <h3>1. Create Test File</h3>
            <a href="/create_test_file" class="btn">Create Test PDF</a>
            <p><small>This will create a test PDF file and redirect to download page</small></p>
        </div>
        
        <div class="test-section">
            <h3>2. Direct Download Tests</h3>
            <a href="/download_file/test_download.pdf" class="btn">Standard Download</a>
            <a href="/test_browser_download/test_download.pdf" class="btn">Browser Compatible Download</a>
            <a href="/download_file/test_merged.pdf" class="btn">Download Existing File</a>
            <p><small>Try different download methods</small></p>
        </div>
        
        <div class="test-section">
            <h3>3. JavaScript Download Test</h3>
            <button onclick="testDownload()" class="btn">JS Download Test</button>
            <p><small>Test download via JavaScript</small></p>
        </div>
        
        <div class="test-section">
            <h3>4. Debug Info</h3>
            <p><strong>Available files:</strong></p>
            <ul>
    """
    
    # List available files
    output_dir = app.config['OUTPUT_FOLDER']
    if os.path.exists(output_dir):
        for file in os.listdir(output_dir):
            if file.endswith('.pdf'):
                file_path = os.path.join(output_dir, file)
                size = os.path.getsize(file_path)
                html += f'<li>{file} ({size} bytes)</li>'
    
    html += """
            </ul>
        </div>
        
        <script>
        function testDownload() {
            console.log('Testing download...');
            
            // Method 1: Direct window.open
            setTimeout(() => {
                window.open('/download_file/test_download.pdf', '_blank');
            }, 100);
            
            // Method 2: Create temporary link
            setTimeout(() => {
                const link = document.createElement('a');
                link.href = '/test_browser_download/test_download.pdf';
                link.download = 'test_download.pdf';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            }, 500);
        }
        
        // Auto-test on page load
        window.addEventListener('load', function() {
            console.log('Page loaded. Download test page ready.');
        });
        </script>
    </body>
    </html>
    """
    
    return html

if __name__ == '__main__':
    print("🌐 Starting browser test server...")
    print("📋 Test URLs:")
    print("   - http://localhost:5000/test_page (comprehensive test page)")
    print("   - http://localhost:5000/create_test_file (create test file)")
    print("   - http://localhost:5000/download_file/test_download.pdf (direct download)")
    print("   - http://localhost:5000/test_browser_download/test_download.pdf (browser compatible)")
    print("\n💡 If download still doesn't work:")
    print("   1. Check browser console for errors (F12)")
    print("   2. Check browser download settings")
    print("   3. Try different browser")
    print("   4. Check if popup blocker is enabled")
    
    app.run(debug=True, port=5000)
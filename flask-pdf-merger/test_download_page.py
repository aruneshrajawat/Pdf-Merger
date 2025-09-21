#!/usr/bin/env python3
"""
Create a test route to directly test the download page
"""

from app import app
from flask import session

@app.route('/test_download')
def test_download():
    """Test route to directly show download page"""
    # Simulate a merged file in session
    session['merged_file'] = {
        'filename': 'test_merged.pdf',
        'pages': 5,
        'size': '2.5 KB'
    }
    
    from flask import render_template
    return render_template('download.html', 
                         filename='test_merged.pdf',
                         pages=5,
                         size='2.5 KB')

if __name__ == '__main__':
    print("🧪 Test server starting...")
    print("📋 Available test routes:")
    print("   - http://localhost:5000/ (main app)")
    print("   - http://localhost:5000/test_download (direct download page test)")
    print("   - http://localhost:5000/history (view merge history)")
    print("\n🔍 To test download button:")
    print("   1. Go to http://localhost:5000/test_download")
    print("   2. You should see a big green 'DOWNLOAD PDF NOW' button")
    print("   3. Click it to test the download")
    
    app.run(debug=True, port=5000)
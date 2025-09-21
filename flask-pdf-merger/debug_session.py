#!/usr/bin/env python3
"""
Debug session data and test upload functionality
"""

from app import app
import os

@app.route('/debug')
def debug_session():
    """Debug route to check session data"""
    from flask import session
    
    debug_info = {
        'session_keys': list(session.keys()),
        'upload_id': session.get('upload_id', 'Not set'),
        'uploaded_files_count': len(session.get('uploaded_files', [])),
        'uploaded_files': session.get('uploaded_files', []),
        'merge_order': session.get('merge_order', 'Not set'),
        'output_name': session.get('output_name', 'Not set'),
        'merged_file': session.get('merged_file', 'Not set'),
        'upload_folder_exists': os.path.exists(app.config['UPLOAD_FOLDER']),
        'output_folder_exists': os.path.exists(app.config['OUTPUT_FOLDER']),
    }
    
    html = "<h1>Debug Session Info</h1>"
    html += "<pre style='background: #f5f5f5; padding: 20px; border-radius: 5px;'>"
    
    for key, value in debug_info.items():
        html += f"<strong>{key}:</strong> {value}\n"
    
    html += "</pre>"
    html += "<br><a href='/'>← Back to Home</a>"
    html += "<br><a href='/merge'>→ Go to Merge Page</a>"
    
    return html

if __name__ == '__main__':
    print("🔍 Debug server starting...")
    print("📋 Available routes:")
    print("   - http://localhost:5000/ (main app)")
    print("   - http://localhost:5000/debug (session debug info)")
    print("   - http://localhost:5000/merge (merge page)")
    print("   - http://localhost:5000/history (history)")
    
    app.run(debug=True, port=5000)
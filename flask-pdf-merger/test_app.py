#!/usr/bin/env python3
"""
Simple test to verify the PDF merger functionality
"""

import os
import tempfile
from app import app

def test_upload_route():
    """Test that the upload route works"""
    with app.test_client() as client:
        # Test GET request to home page
        response = client.get('/')
        assert response.status_code == 200
        print("✓ Home page loads successfully")
        
        # Test merge page without files (should redirect)
        response = client.get('/merge')
        assert response.status_code == 302  # Redirect
        print("✓ Merge page redirects when no files uploaded")
        
        # Test history page
        response = client.get('/history')
        assert response.status_code == 200
        print("✓ History page loads successfully")

if __name__ == "__main__":
    print("Testing PDF Merger App...")
    test_upload_route()
    print("All tests passed! ✓")
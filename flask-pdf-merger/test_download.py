#!/usr/bin/env python3
"""
Test download functionality
"""

from app import app
import os

def test_download():
    """Test the download functionality"""
    with app.test_client() as client:
        # Check if test file exists
        test_file = 'output/test_merged.pdf'
        if os.path.exists(test_file):
            print(f"✅ Test file exists: {test_file}")
            
            # Test download page
            response = client.get('/download/test_merged.pdf')
            print(f"Download page status: {response.status_code}")
            
            if response.status_code == 200:
                print("✅ Download page loads successfully")
                
                # Test actual file download
                response = client.get('/download_file/test_merged.pdf')
                print(f"File download status: {response.status_code}")
                
                if response.status_code == 200:
                    print("✅ File download works!")
                    print(f"Content-Type: {response.headers.get('Content-Type')}")
                    print(f"Content-Length: {response.headers.get('Content-Length')}")
                    return True
                else:
                    print(f"❌ File download failed: {response.status_code}")
            else:
                print(f"❌ Download page failed: {response.status_code}")
        else:
            print(f"❌ Test file doesn't exist: {test_file}")
            
            # Create test file
            print("Creating test file...")
            response = client.get('/create_test_file')
            print(f"Create test file status: {response.status_code}")
            
            if response.status_code == 302:  # Redirect to download page
                print("✅ Test file created, testing download...")
                return test_download()  # Retry
    
    return False

if __name__ == "__main__":
    print("🧪 Testing download functionality...")
    print("=" * 40)
    
    success = test_download()
    
    if success:
        print("\n🎉 Download test passed!")
        print("📋 To test manually:")
        print("   1. Start server: python3 debug_session.py")
        print("   2. Go to: http://localhost:5000/create_test_file")
        print("   3. Click the download button")
    else:
        print("\n❌ Download test failed!")
        print("Check the debug output above for details.")
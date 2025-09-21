#!/usr/bin/env python3
"""
Test direct download with browser simulation
"""

from app import app
import os

def test_direct_download():
    """Test download with requests library (simulates browser)"""
    
    # Start the app in test mode
    with app.test_client() as client:
        # First, create a test file
        print("1. Creating test file...")
        response = client.get('/create_test_file')
        print(f"   Create test file response: {response.status_code}")
        
        if response.status_code == 302:  # Redirect to download page
            print("   ✅ Test file created")
            
            # Test the download
            print("2. Testing download...")
            response = client.get('/download_file/test_download.pdf')
            print(f"   Download response status: {response.status_code}")
            print(f"   Content-Type: {response.headers.get('Content-Type')}")
            print(f"   Content-Length: {response.headers.get('Content-Length')}")
            print(f"   Content-Disposition: {response.headers.get('Content-Disposition')}")
            
            if response.status_code == 200:
                print("   ✅ Download successful!")
                
                # Save the downloaded content to verify
                with open('downloaded_test.pdf', 'wb') as f:
                    f.write(response.data)
                
                print(f"   ✅ File saved as 'downloaded_test.pdf' ({len(response.data)} bytes)")
                return True
            else:
                print(f"   ❌ Download failed with status {response.status_code}")
                print(f"   Response: {response.data.decode()}")
        else:
            print(f"   ❌ Failed to create test file: {response.status_code}")
    
    return False

def check_file_permissions():
    """Check if output files have correct permissions"""
    output_dir = 'output'
    if os.path.exists(output_dir):
        print(f"📁 Output directory: {os.path.abspath(output_dir)}")
        print(f"   Permissions: {oct(os.stat(output_dir).st_mode)[-3:]}")
        
        for file in os.listdir(output_dir):
            file_path = os.path.join(output_dir, file)
            if file.endswith('.pdf'):
                print(f"📄 {file}:")
                print(f"   Size: {os.path.getsize(file_path)} bytes")
                print(f"   Permissions: {oct(os.stat(file_path).st_mode)[-3:]}")
                print(f"   Readable: {os.access(file_path, os.R_OK)}")

if __name__ == "__main__":
    print("🧪 Testing direct download functionality...")
    print("=" * 50)
    
    print("\n📋 Checking file permissions...")
    check_file_permissions()
    
    print("\n🔄 Testing download...")
    success = test_direct_download()
    
    if success:
        print("\n🎉 Download test successful!")
        print("📋 The download should work in your browser.")
        print("💡 If it still doesn't work, try:")
        print("   1. Different browser (Chrome, Firefox, Safari)")
        print("   2. Disable ad blockers")
        print("   3. Check browser download settings")
        print("   4. Try right-click → Save As")
    else:
        print("\n❌ Download test failed!")
        print("Check the debug output above.")
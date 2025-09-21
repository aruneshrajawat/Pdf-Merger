#!/usr/bin/env python3
"""
Test file reordering functionality
"""

from app import app
import json

def test_reorder():
    """Test the reorder functionality"""
    with app.test_client() as client:
        with client.session_transaction() as sess:
            # Set up test files in session
            sess['uploaded_files'] = [
                {'name': 'file1.pdf', 'path': '/test/file1.pdf', 'pages': 5, 'size': '100 KB'},
                {'name': 'file2.pdf', 'path': '/test/file2.pdf', 'pages': 3, 'size': '80 KB'},
                {'name': 'file3.pdf', 'path': '/test/file3.pdf', 'pages': 7, 'size': '150 KB'}
            ]
        
        print("1. Testing merge page with files...")
        response = client.get('/merge')
        print(f"   Merge page status: {response.status_code}")
        
        if response.status_code == 200:
            print("   ✅ Merge page loads with files")
            
            print("2. Testing file reordering...")
            # Test reordering: move file3 to first position
            new_order = ['file3.pdf', 'file1.pdf', 'file2.pdf']
            
            response = client.post('/reorder', 
                                 data=json.dumps({'order': new_order}),
                                 content_type='application/json')
            
            print(f"   Reorder response: {response.status_code}")
            
            if response.status_code == 200:
                result = response.get_json()
                print(f"   Reorder result: {result}")
                
                if result['status'] == 'success':
                    print("   ✅ Files reordered successfully")
                    
                    # Check if session was updated
                    with client.session_transaction() as sess:
                        files = sess.get('uploaded_files', [])
                        file_names = [f['name'] for f in files]
                        print(f"   New order in session: {file_names}")
                        
                        if file_names == new_order:
                            print("   ✅ Session updated correctly")
                            return True
                        else:
                            print(f"   ❌ Session not updated correctly. Expected: {new_order}, Got: {file_names}")
                else:
                    print(f"   ❌ Reorder failed: {result.get('message')}")
            else:
                print(f"   ❌ Reorder request failed: {response.status_code}")
        else:
            print(f"   ❌ Merge page failed: {response.status_code}")
    
    return False

if __name__ == "__main__":
    print("🧪 Testing file reordering functionality...")
    print("=" * 50)
    
    success = test_reorder()
    
    if success:
        print("\n🎉 Reorder test passed!")
        print("📋 Features available:")
        print("   - Drag and drop to reorder files")
        print("   - Up/Down arrow buttons")
        print("   - Remove files from merge")
        print("   - Real-time order saving")
    else:
        print("\n❌ Reorder test failed!")
        print("Check the debug output above.")
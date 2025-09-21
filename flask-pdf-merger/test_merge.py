#!/usr/bin/env python3
"""
Test merge functionality
"""
import requests
import os

def test_merge():
    base_url = "http://localhost:5000"
    
    # Test if server is running
    try:
        response = requests.get(base_url)
        print(f"✅ Server is running: {response.status_code}")
    except:
        print("❌ Server is not running. Start with: python app.py")
        return
    
    # Test recovery of existing session
    session_id = "10972494-9868-48a7-89f9-325091aee585"
    recovery_url = f"{base_url}/recover/{session_id}"
    
    try:
        response = requests.get(recovery_url, allow_redirects=False)
        print(f"✅ Recovery URL works: {response.status_code}")
        
        # Follow redirect to merge page
        if response.status_code in [302, 301]:
            merge_url = f"{base_url}/merge"
            response = requests.get(merge_url)
            print(f"✅ Merge page accessible: {response.status_code}")
            
            if "files ready to merge" in response.text:
                print("✅ Files found on merge page")
            else:
                print("❌ No files found on merge page")
                
    except Exception as e:
        print(f"❌ Error testing recovery: {e}")

if __name__ == "__main__":
    test_merge()
#!/usr/bin/env python3
"""
Quick fix script to help recover uploaded files
"""
import os
import json

def find_uploaded_files():
    uploads_dir = 'uploads'
    if not os.path.exists(uploads_dir):
        print("No uploads directory found")
        return
    
    print("Found uploaded files:")
    print("=" * 50)
    
    for session_id in os.listdir(uploads_dir):
        session_path = os.path.join(uploads_dir, session_id)
        if os.path.isdir(session_path):
            print(f"\nSession ID: {session_id}")
            files = [f for f in os.listdir(session_path) if f.endswith('.pdf')]
            print(f"Files ({len(files)}):")
            for file in files:
                file_path = os.path.join(session_path, file)
                size = os.path.getsize(file_path)
                print(f"  - {file} ({size/1024:.1f} KB)")
            
            print(f"\nTo recover this session, visit:")
            print(f"http://localhost:5000/recover/{session_id}")

if __name__ == "__main__":
    find_uploaded_files()
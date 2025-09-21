#!/usr/bin/env python3
import os
import shutil

# Create a simple test file
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# Copy sample PDF to output
if os.path.exists('sample_pdfs/sample1.pdf'):
    shutil.copy2('sample_pdfs/sample1.pdf', 'output/test_download.pdf')
    print("✅ Created test_download.pdf")
    print("File size:", os.path.getsize('output/test_download.pdf'), "bytes")
else:
    # Create minimal text file as fallback
    with open('output/test_download.pdf', 'w') as f:
        f.write("Test PDF content")
    print("✅ Created minimal test file")

print("Test download at: http://localhost:5000/download_file/test_download.pdf")
from flask import Flask, request, send_file, render_template_string
import os
from PyPDF2 import PdfReader, PdfWriter

app = Flask(__name__)

# Create output directory
os.makedirs('output', exist_ok=True)

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html>
<head><title>Simple PDF Merger</title></head>
<body>
    <h1>PDF Merger</h1>
    <form action="/merge" method="post" enctype="multipart/form-data">
        <input type="file" name="files" multiple accept=".pdf" required>
        <br><br>
        <button type="submit">MERGE PDFs</button>
    </form>
</body>
</html>
    ''')

@app.route('/merge', methods=['POST'])
def merge():
    files = request.files.getlist('files')
    if not files:
        return "No files selected"
    
    # Merge PDFs
    writer = PdfWriter()
    for file in files:
        if file.filename.endswith('.pdf'):
            reader = PdfReader(file)
            for page in reader.pages:
                writer.add_page(page)
    
    # Save merged PDF
    output_path = 'output/merged.pdf'
    with open(output_path, 'wb') as f:
        writer.write(f)
    
    return f'<h1>Success!</h1><a href="/download">Download Merged PDF</a>'

@app.route('/download')
def download():
    return send_file('output/merged.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
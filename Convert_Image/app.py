import os
import io
import zipfile
from flask import Flask, request, send_file, render_template_string
from werkzeug.utils import secure_filename
from convertImage import downscale_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['COMPRESSED_FOLDER'] = 'compressed'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB max upload size

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['COMPRESSED_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    # Serve the frontend HTML directly from a string for simplicity
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Image Compressor</title>
        <link rel="stylesheet" href="/style.css" />
    </head>
    <body>
        <div class="container">
            <h1>Image Compressor</h1>
            <div id="dropArea">
                <p>Drag and drop images here or click to select files</p>
                <input type="file" id="fileElem" multiple accept="image/*" style="display:none" />
                <label class="button" for="fileElem">Select Images</label>
            </div>
            <div id="fileList"></div>
            <button id="uploadBtn" disabled>Upload and Compress</button>
            <div id="downloadLinks"></div>
        </div>
        <script src="/script.js"></script>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/style.css')
def style_css():
    css_content = """
    body {
        font-family: Arial, sans-serif;
        margin: 20px;
        background-color: #f4f4f4;
    }
    .container {
        max-width: 600px;
        margin: auto;
        background: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    #dropArea {
        border: 2px dashed #ccc;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        color: #999;
        margin-bottom: 10px;
        cursor: pointer;
    }
    #dropArea.dragover {
        border-color: #333;
        color: #333;
    }
    .button {
        background-color: #007bff;
        color: white;
        padding: 8px 12px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        display: inline-block;
        margin-top: 10px;
    }
    .button:disabled {
        background-color: #aaa;
        cursor: not-allowed;
    }
    #fileList ul {
        list-style: none;
        padding-left: 0;
    }
    #fileList li {
        margin-bottom: 5px;
    }
    #downloadLinks a {
        display: block;
        margin-top: 10px;
        color: #007bff;
        text-decoration: none;
    }
    """
    return css_content, 200, {'Content-Type': 'text/css'}

@app.route('/script.js')
def script_js():
    js_content = """
    const dropArea = document.getElementById('dropArea');
    const fileElem = document.getElementById('fileElem');
    const fileList = document.getElementById('fileList');
    const uploadBtn = document.getElementById('uploadBtn');
    const downloadLinks = document.getElementById('downloadLinks');

    let filesToUpload = [];

    dropArea.addEventListener('dragenter', (e) => {
        e.preventDefault();
        dropArea.classList.add('dragover');
    });

    dropArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropArea.classList.add('dragover');
    });

    dropArea.addEventListener('dragleave', (e) => {
        e.preventDefault();
        dropArea.classList.remove('dragover');
    });

    dropArea.addEventListener('drop', (e) => {
        e.preventDefault();
        dropArea.classList.remove('dragover');
        const files = e.dataTransfer.files;
        handleFiles(files);
    });

    dropArea.addEventListener('click', () => {
        fileElem.click();
    });

    fileElem.addEventListener('change', () => {
        handleFiles(fileElem.files);
    });

    function handleFiles(files) {
        filesToUpload = Array.from(files);
        if (filesToUpload.length > 0) {
            fileList.innerHTML = '<strong>Selected files:</strong><ul>' + 
                filesToUpload.map(file => `<li>${file.name}</li>`).join('') + 
                '</ul>';
            uploadBtn.disabled = false;
            downloadLinks.innerHTML = '';
        } else {
            fileList.innerHTML = 'No files selected.';
            uploadBtn.disabled = true;
        }
    }

    uploadBtn.addEventListener('click', () => {
        if (filesToUpload.length === 0) return;
        uploadBtn.disabled = true;
        downloadLinks.innerHTML = 'Uploading and compressing...';

        const formData = new FormData();
        filesToUpload.forEach(file => {
            formData.append('images', file);
        });

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) throw new Error('Upload failed');
            return response.blob();
        })
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'compressed_images.zip';
            a.textContent = 'Download Compressed Images';
            downloadLinks.innerHTML = '';
            downloadLinks.appendChild(a);
            uploadBtn.disabled = false;
        })
        .catch(err => {
            downloadLinks.innerHTML = 'Error: ' + err.message;
            uploadBtn.disabled = false;
        });
    });
    """
    return js_content, 200, {'Content-Type': 'application/javascript'}

@app.route('/upload', methods=['POST'])
def upload():
    if 'images' not in request.files:
        return 'No images part in the request', 400

    files = request.files.getlist('images')
    if not files:
        return 'No images uploaded', 400

    # Clear previous files
    for folder in [app.config['UPLOAD_FOLDER'], app.config['COMPRESSED_FOLDER']]:
        for f in os.listdir(folder):
            os.remove(os.path.join(folder, f))

    compressed_files = []

    for file in files:
        filename = secure_filename(file.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)

        compressed_filename = f"compressed_{filename}"
        compressed_path = os.path.join(app.config['COMPRESSED_FOLDER'], compressed_filename)

        try:
            downscale_image(upload_path, compressed_path)
            compressed_files.append(compressed_path)
        except Exception as e:
            print(f"Error compressing {filename}: {e}")

    # Create a zip archive of compressed images in memory
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for file_path in compressed_files:
            zip_file.write(file_path, os.path.basename(file_path))
    zip_buffer.seek(0)

    return send_file(
        zip_buffer,
        mimetype='application/zip',
        as_attachment=True,
        download_name='compressed_images.zip'
    )

if __name__ == '__main__':
    app.run(debug=True)

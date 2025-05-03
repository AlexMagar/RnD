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

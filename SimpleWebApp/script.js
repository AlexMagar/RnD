document.getElementById('actionButton').addEventListener('click', function() {
    const displayText = document.getElementById('displayText');
    if (displayText.textContent === 'Hello! Click the button to change this text.') {
        displayText.textContent = 'You clicked the button! This is a simple web app.';
    } else {
        displayText.textContent = 'Hello! Click the button to change this text.';
    }
});

const dropArea = document.getElementById('dropArea');
const fileList = document.getElementById('fileList');

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
    if (files.length > 0) {
        fileList.innerHTML = '<strong>Dropped files:</strong><ul>' + 
            Array.from(files).map(file => `<li>${file.name}</li>`).join('') + 
            '</ul>';
    } else {
        fileList.innerHTML = 'No files dropped.';
    }
});

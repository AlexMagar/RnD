document.getElementById('actionButton').addEventListener('click', function() {
    const displayText = document.getElementById('displayText');
    if (displayText.textContent === 'Hello! Click the button to change this text.') {
        displayText.textContent = 'You clicked the button! This is a simple web app.';
    } else {
        displayText.textContent = 'Hello! Click the button to change this text.';
    }
});

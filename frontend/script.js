// frontend/script.js
document.getElementById('dataForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let value1 = document.getElementById('value1').value;
    let value2 = document.getElementById('value2').value;

    // Perform validation
    if (value1 === '' || value2 === '') {
        alert('Both fields are required!');
        return;
    }

    // Send data to backend
    fetch('/api/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ value1, value2 })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
});

document.getElementById('wineForm').addEventListener('submit', function(e) {
    const inputs = document.querySelectorAll('input[type="number"]');
    let valid = true;

    inputs.forEach(input => {
        if (!input.value || input.value < 0) {
            valid = false;
            input.style.borderColor = 'red';
        } else {
            input.style.borderColor = '#ccc';
        }
    });

    if (!valid) {
        e.preventDefault();
        alert('Please fill all fields with valid positive numbers.');
    }
});

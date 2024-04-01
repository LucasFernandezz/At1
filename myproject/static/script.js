// script.js

document.addEventListener('DOMContentLoaded', function () {
    const inputBox = document.querySelector('.number-input');
    const enterButton = document.querySelector('.enter-button');
    const clearDotsButton = document.querySelector('.clear-dots-button');
    const numberTable = document.querySelector('.number-table tbody');

    // Event listener for input change
    inputBox.addEventListener('input', function () {
        // Enable button if input has 8 characters, disable otherwise
        enterButton.disabled = inputBox.value.length !== 8;
    });

    // Event listener for Enter button click
    enterButton.addEventListener('click', function () {
        // Send the input number to the backend
        const number = inputBox.value;
        fetch('/save_number/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ number: number })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // If the number is saved successfully, add it to the table
                const row = document.createElement('tr');
                row.innerHTML = `<td>${data.user}</td><td>${number}</td>`;
                numberTable.appendChild(row);
            } else {
                // Handle error (e.g., display error message)
                console.error(data.message);
            }
        });
    });

    // Event listener for Clear Dots button click
    clearDotsButton.addEventListener('click', function () {
        // Remove all red dots from the image container
        const redDots = document.querySelectorAll('.red-dot');
        redDots.forEach(dot => dot.remove());
    });

    // Function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

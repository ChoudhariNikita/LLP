// Function to check if passwords match
function checkPasswordMatch() {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const passwordMessage = document.getElementById('passwordMessage');

    if (password === confirmPassword) {
        passwordMessage.innerHTML = 'Passwords match';
        passwordMessage.style.color = 'green';
        document.getElementById('registerButton').disabled = false;
    } else {
        passwordMessage.innerHTML = 'Passwords do not match';
        passwordMessage.style.color = 'red';
        document.getElementById('registerButton').disabled = true;
    }
}

// Attach the checkPasswordMatch function to the confirmPassword input
document.getElementById('confirmPassword').addEventListener('input', checkPasswordMatch);

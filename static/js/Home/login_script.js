// Function to check if passwords match
function checkPasswordMatch() {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const passwordMessage = document.getElementById('passwordMessage');
    const passwordHelp = document.getElementById('passwordHelp');
    const passhelp2=document.getElementById('help');
    const registerButton = document.getElementById('registerButton');

    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_@$!%*#?&])[A-Za-z\d_@$!%*#?&]{8,}$/;

    if (password === confirmPassword) {
        passwordMessage.innerHTML = 'Passwords match!!';
        passwordMessage.style.color = 'green';
    } else {
        passwordMessage.innerHTML = 'Passwords do not match!!';
        passwordMessage.style.color = 'red';
        passhelp2.style.color='purple';
    }

    if (!passwordRegex.test(password)) {
        passwordHelp.innerHTML = "Password should contain at least one uppercase letter, one lowercase letter, one digit, one special character (_@$!%*#?&), and should be at least 8 characters long.";
        passhelp2.innerHTML="Fullfill criteria for password.!";
        registerButton.disabled = true;
    } else {
        passwordHelp.innerHTML = "";
        if (password === confirmPassword) {
            registerButton.disabled = false;
        }
    }
}

// Attach the checkPasswordMatch function to the confirmPassword input
document.getElementById('confirmPassword').addEventListener('input', checkPasswordMatch);

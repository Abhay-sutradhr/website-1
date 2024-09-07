document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent form submission

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // You can add your login logic here (e.g., check credentials, make an API call, etc.)
    // For demonstration purposes, let's just log the input values.
    console.log('Username:', username);
    console.log('Password:', password);
});

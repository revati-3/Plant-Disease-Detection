function togglePassword() {
    let pass = document.getElementById("password");
    pass.type = pass.type === "password" ? "text" : "password";
}

// Simple form validation
document.getElementById("loginForm").addEventListener("submit", function(e) {
    e.preventDefault();
    alert("Login Successful (Demo)");
});
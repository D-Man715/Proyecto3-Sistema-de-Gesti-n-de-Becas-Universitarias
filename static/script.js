
// ----------------------------------login-----------------------------

function login() {
    const token = localStorage.getItem('token');
    const datos = {
        username: document.getElementById('username').value,
        password: document.getElementById('password').value
    };

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datos)
    })
    .then(res => res.json())
    .then(data => {
        if (data.access_token) {
            localStorage.setItem('token', data.access_token);
            document.getElementById('mensaje').textContent = 'Login correcto';
            document.getElementById('mensaje').className = 'mt-3 fw-bold text-success';
        } else {
            document.getElementById('mensaje').textContent = data.error || 'Credenciales incorrectas';
            document.getElementById('mensaje').className = 'mt-3 fw-bold text-danger';
        }
    });
    location.reload();
}

function logout() {
    localStorage.removeItem('token');
    document.getElementById('mensaje').textContent = 'Sesión cerrada';
    document.getElementById('mensaje').className = 'mt-3 fw-bold text-warning';
    location.reload();
}
//------------------------------------------------------------------------------------------
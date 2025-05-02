
// perform the network request and return whatever JSON the server returns
async function makeRequest(endpoint, method = 'GET', body = null) {
    
    const options = { method: method.toUpperCase(),};
  
    if (body && method.toUpperCase() !== 'GET') {
        options.body = JSON.stringify(body);
        options.headers = {'Content-Type': 'application/json'}; 
    }
  
    return fetch(endpoint, options)
        .then(response => {
            if (!response.ok) {
            return response.json().then(err => {
                throw new Error(err.message || 'Request failed');
                });
            }
            return response.json();
    });
}

function toggleDarkMode() {
    const body = document.getElementsByTagName('body')[0];
    const dark_mode_btn = document.getElementById('dark-mode-button');
    if (body.className == "dark-mode") { body.className = "light-mode"; dark_mode_btn.innerHTML = '&#127774;' }
    else { body.className = "dark-mode"; dark_mode_btn.innerHTML = '&#127769;' }
}

// when the DOM loads execute these JS functions
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("dark-mode-button").addEventListener('click', toggleDarkMode);
});
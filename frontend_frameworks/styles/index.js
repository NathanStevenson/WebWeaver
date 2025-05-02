
// perform the network request and return whatever JSON the server returns
async function makeRequest(endpoint, method = 'GET', body = null) {
    const options = {
      method: method.toUpperCase(),
      headers: {'Content-Type': 'application/json' },
    };
  
    if (body && method.toUpperCase() !== 'GET') {
      options.body = JSON.stringify(body);
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
    if (body.className == "dark-mode") { body.className = "light-mode"; }
    else { body.className = "dark-mode"; }
}
document.getElementById("call-form").addEventListener("submit", function (event) {
    event.preventDefault();
    const toNumber = document.getElementById("phone-number").value;

    fetch('/make_call', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            to_number: toNumber
        })
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById("call-status").innerText = data;
    })
    .catch(error => {
        document.getElementById("call-status").innerText = 'Error initiating call!';
        console.error('Error:', error);
    });
});

document.getElementById("speaker").addEventListener("click", function () {
    // Handle speaker functionality here
    alert('Speaker functionality not implemented yet.');
});

document.getElementById("mute").addEventListener("click", function () {
    // Handle mute/unmute functionality here
    alert('Mute functionality not implemented yet.');
});

document.getElementById("hold").addEventListener("click", function () {
    // Handle hold/unhold functionality here
    alert('Hold functionality not implemented yet.');
});
                                                    

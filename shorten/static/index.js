myForm = document.getElementById('myForm')

myForm.addEventListener('submit', getShort)

function getShort(e) {
    e.preventDefault()
    let longURL = e.target[0].value

    // fetch(`http://localhost:8000/url/${longURL}`)
    //     .then(response => response.json)
    //     .then(data => console.log(data))

    fetch('http://localhost:8000/url/', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(longURL),
    })
    .then(response => response.json)
    .then(data => console.log(data))
}
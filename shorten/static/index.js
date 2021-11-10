myForm = document.getElementById('myForm')

myForm.addEventListener('submit', getShort)

function getShort(e) {
    e.preventDefault()
    let longURL = e.target[0].value
    console.log(JSON.stringify(longURL))

    data = {
        "url": longURL
    }


    fetch('http://127.0.0.1:8000/url/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
           
        },

        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => console.log(data))
}
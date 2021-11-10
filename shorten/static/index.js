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
        .then(r => r.json())
        .then(r => r.path)
        .then(r => addNew(r))



    function addNew(u) {
        console.log(u)
        let newURL = document.createElement("a")
        console.log(u)
        newURL.textContent = `http://localhost:8000/url/${u}`
        console.log(newURL.textContent)
        document.getElementById('mainBody').appendChild(newURL)


        fetch(newURL.textContent)
            .then(r => r.json())
            .then(r => r.url)
            .then(r => linkButton(r))



        function linkButton(m) {
            let newButton = document.createElement("a")
            console.log(m)
            newButton.textContent = 'Visit your link'
            newButton.href = m
            newButton.setAttribute('class', 'myNewButton')
            console.log(newButton.textContent)
            document.getElementById('mainBody').appendChild(document.createElement("br"))
            document.getElementById('mainBody').appendChild(newButton)
        }



    }


}


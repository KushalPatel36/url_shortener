# URL shortener

## Functionality
A Url shortening tool which does the following:
* Users should be able to enter a url into an input box on your website's front page.
* If User tries to access your website with a path you have stored in your database, they should get rerouted to the URL it relates to.

## Installation
* Create the virtual environemnt with `pipenv shell`
* Run `pipenv install` to install packages
* Run `python manage.py runserver` to run the server which should open on localhost:8000
* Navigate to `http://localhost:8000/url/home` to enter the homepage where you can enter your url and click the shorten url button
* Then you are presented with your shortened link


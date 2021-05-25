# React-Flask challenge

## Problem 2 - Setting up the back-end service

I created a simple API with [Flask](https://flask.palletsprojects.com/en/2.0.x/). I've always built things in Django before, but I felt it would've been way overkill for a simple API request with no database connection. Flask is super easy to set up on the other hand.

You can start the app in local by running `flask run`.

The API has a single endpoint with the relative path of `/<roman>`. Upon a GET request, it will return an object that meets the specs of the problem.
![output](curl_output.png)

I created 2 functions that helped me generate the object:

1. `r2d` from `roman2decimal.py` - converts a Roman numeral string to a decimal value in `int`
2. `bc` from `base_convert.py` - converts a decimal value in `int` to any other base that's been input as `str`

I import these 2 functions into `main.py` that serves as the API's main file.

I use [flask-CORS](https://flask-cors.readthedocs.io/en/latest/) to allow cross-origin AJAX from front-end (needed for problem 3).

## Problem 4

Link to [live site](https://mihailthebuilder.github.io/react-flask-challenge-3-and-4/).

See [this repo](https://github.com/mihailthebuilder/react-flask-challenge-3-and-4) for instructions on hosting the front-end.

### Hosting back-end in the cloud

I use [Heroku](https://www.heroku.com) to host the back-end API.

Install `gunicorn`: `pip install gunicorn`

Create `wsgi.py` file that references the main app file `main.py`.

Install Heroku on your linux OS with Snapcraft: `sudo snap install heroku --classic`

Make sure you have a Heroku account, then log into it with `heroku login`

Create Heroku app: `heroku create`

Set git remote to the app: `heroku git:remote -a desolate-harbor-87386`

Deploy the app: `git push heroku main`

from app import app
from flask import render_template


@app.route('/favoritefive')
def favoritefive():

   # context = dict(
    #customer_name = "George"
    #customer_username = "greynolds")

    context = {
      "persons_name": "George's",
       # "customer_username": "greynolds",
        "items": {
            1: 'Kobe Bryant',
            2: 'Stephen Curry',
            3: 'Lebron James',
            4: 'Kevin Durant',
            5: 'Shaquille ONeal'
        }
    }
    return render_template('favoritefive.html', **context)


@app.route('/')
def index():
    return render_template('index.html')

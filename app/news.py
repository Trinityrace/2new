from flask import render_template
from app import app

# News
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'World news today'
    return render_template('index.html',message = message)
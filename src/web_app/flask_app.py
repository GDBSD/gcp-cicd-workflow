# -*- coding: utf-8 -*-

"""
"from flask import Flask"  creates an object which refers to the entirety of the app itself. 
When we state "app = Flask(__name__)", we are creating the variable app which represents our 
application. Therefore, when we configure the variable app, we’re configuring the way our entire 
application works.

To run the app, from the command line:
export FLASK_APP=flask_app.py
flask run
"""

from flask import Flask

app = Flask(__name__)


# Home page
@app.route('/')
def hello_world():
    return 'Hello, World!'

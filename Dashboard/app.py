#import dependencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
# import scraping
import random
# import requests
from config import MONGO_URI
import os


#set up flask
app = Flask(__name__)

#Use pyMondo to set up mongo connection
app.config["MONGO_URI"] = os.environ.get(MONGO_URI)
mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)












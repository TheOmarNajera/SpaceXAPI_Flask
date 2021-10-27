from flask import Flask, render_template
import requests

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

URL = 'https://api.spacexdata.com/v4/rockets'

@app.route('/')
def index():
    data = requests.get(URL)
    data = data.json()
    return render_template('index.html', data=data)
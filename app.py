from flask import Flask
from jinja2 import Markup

#from jinja2.utils import markupsafe.

#markupsafe.Markup()

#Markup('')

app = Flask(__name__)


import requests

@app.route('/')
def ping_service():
    return 'Pong'

@app.route('/ping')
def do_ping():
    ping = 'Ping ...'

    response = ''
    try:
        response = requests.get('http://pong-service-container:5001/pong')
    except requests.exceptions.RequestException as e:
        print('\n Pong')
        return 'Pong ...\n'

    return 'Pong ... ' + response.text + ' \n'

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)



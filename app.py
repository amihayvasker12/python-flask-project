from flask import Flask
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
        print('\n Cannot reach the pong service.')
        return 'Pong ...\n'

    return 'Pong ... ' + response.text + ' \n'

if __name__ == "__main__":
    app.run(host ='3.19.142.70', port = 5000, debug = True)

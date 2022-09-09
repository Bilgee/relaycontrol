# app.py
from flask import Flask, request
from log import logger
from config import RELAY
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Helllo World!</h1>'

@app.route('/relay/open', methods=['POST'])
def relay():
    response = {
        u"response": {
            u"status": 2,
            u"msg": 'Unknown error'
        }
    }
    try:
        content = request.json
        if content['action'] =='open':
            URL = RELAY['IN'] if entry =='IN' else RELAY['OUT']
            data = {'type':0, 'relay':0, 'on':1, 'time':5, 'pwd':4660}
            logger.info('sending relay data')
            relay = requests.get(url = RELAY['IN'], params=data, timeout=5)
            logger.info(relay)
            if relay.status_code == 200:
                response['response']['status'] = 0
                response['response']['msg'] = 'successfull'
        else:
            response['response']['status'] = 1
            response['response']['msg'] = 'request received'
        return response
    except:
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
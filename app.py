#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response
import random
import string

app = Flask(__name__)

# Constant word list.
cache = {}
subscriber = set()

#error handler
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

#GET api to get reference of word list
@app.route('/api/v1/subscribe', methods=['GET'])
def get_subsriber_key():
    subscribe_key = ''.join((random.choice(string.ascii_lowercase) for x in range(10)))
    subscriber.add(subscribe_key)
    return subscribe_key


@app.route('/api/v1/getkey', methods=['GET'])
def get_key():
    if 'subscribe_id' in request.args:
        id = request.args['subscribe_id']
        if id not in subscriber:
            return "Error: Wrong subscribe_id. Please create new or existing subscription."
        if 'key' in request.args:
            key = request.args['key']
            if key not in cache:
                return "Error: Key does not exist"
            return cache.get(key)
        else:
            return "Error: No key field provided. Please specify an key."
    else:
        return "Error: No subscribe_id field provided. Please specify an subscribe_id."

@app.route('/api/v1/putkeyvalue', methods=['POST'])
def put_key():
    if 'subscribe_id' in request.args:
        id = request.args['subscribe_id']
        if id not in subscriber:
            return "Error: Wrong subscribe_id. Please create new or existing subscription."
        if 'key' not in request.args:
            return "Error: No key field provided. Please specify an key."
        key = request.args['key']
        if 'value' not in request.args:
            return "Error: No value field provided. Please specify an value."
        value = request.args['value']
        cache[key]=value
        return "Success: key:value updated"
    else:
        return "Error: No subscribe_id field provided. Please specify an subscribe_id."


if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0")
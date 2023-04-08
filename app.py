import os
import json
from flask import Flask, request

PORT = int(os.environ.get('PORT', 5050))

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def catch_all(path):
    url = request.url
    headers = dict(request.headers)
    query_params = dict(request.args)
    try:
        body = request.get_json()
    except:
        body = request.data.decode('utf-8')
    return {
        'method': request.method,
        'url': url,
        'path': path,
        'headers': headers,
        'query_params': query_params,
        'body': body
    }

if __name__ == '__main__':
    app.run(debug=True, port=PORT)

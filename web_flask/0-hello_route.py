#!/usr/bin/python3
""" a simple flask web server """
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False, methods=['GET'])
def home():
    """ home route """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
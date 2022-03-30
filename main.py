import json
import datetime
import time

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

from flask import Flask, request, render_template

app = Flask(__name__)
app.config.from_object(__name__)
@app.route("/")
def index():
    return "doutei"
def main():
    print("hello work")
    app.debug=True
    host="localhost"
    port=5454
    host_port=(host,port)
    server=WSGIServer(
        host_port,
        app
    )
    server.serve_forever()
if __name__ == '__main__':
    main()
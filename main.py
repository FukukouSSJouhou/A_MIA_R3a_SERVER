import json
import datetime
import random
import time

import numpy as np
from PIL import Image
from gevent.pywsgi import WSGIServer
import cv2
from flask import Flask, request, render_template
app = Flask(__name__)
app.config.from_object(__name__)
@app.route("/")
def index():
    return "doutei"
@app.route("/posttest",methods=["GET","POST"])
def posttest():
    if request.method=="POST":
        #datakun=request.stream.read()
        #img1 = cv2.imdecode(datakun, flags=cv2.IMREAD_GRAYSCALE)
        #if(img1!=[]):
       #     print(img1)
        img_pil = Image.open(request.stream)
        img_numpy=np.asarray(img_pil)
        img_numpy_bgr = cv2.cvtColor(img_numpy, cv2.COLOR_RGBA2BGR)
        return "POST" + str(random.random())
    else:
        return "GET" + str(random.random())

def main():
    print("hello work")
    app.debug=True
    host='0.0.0.0'
    port=5454
    host_port=(host,port)
    server=WSGIServer(
        host_port,
        app
    )
    server.serve_forever()
if __name__ == '__main__':
    main()
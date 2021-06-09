from flask import Flask
from flask import json

import logging

app = Flask(__name__)


@app.route("/status")
def status():
    response=app.response_class(
    response=json.dumps({"result":"Ok-healthy"}),
    status=200,
    mimetype='application/json'
    )
    
    ##log 
    app.logger.info("Status Request was successfull")
    
    return response

@app.route("/metrics")
def metrics():
    response=app.response_class(
    response=json.dumps({"status":"success","code":0,"data":{"Usercount":140,"UserCountActive":23}}),
    status=200,
    mimetype='application/json'
    )
    
    app.logger.info("Metrics request was successfull")
    
    return response
    


@app.route("/")
def hello():
    app.logger.info("Main request successfull")
    return "Hello World!"

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')






# Awful security risk, test for the codeql scanner.
"""
export FLASK_APP=unsafe.py
python -m flask run

In browser, open 
http://127.0.0.1:5000/print("never%20do%20this")

"""
from flask import Flask
import logging
app = Flask(__name__)

@app.route('/<command>')
def run_command(command):
    logging.log(logging.WARNING, "about to run '{}'".format(command))
    exec(command)
    return "done"
    

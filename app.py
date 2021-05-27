'''
Source:

Author: Raja CSP


'''
from flask import Flask,render_template, jsonify, request
import random
import json
import data as dt


app  = Flask(__name__)
PORT = 3000

@app.route("/", methods=["GET","POST"])
def startpy():
    
    pnl = dt.getpnl()

    return render_template("date.html") 



if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)
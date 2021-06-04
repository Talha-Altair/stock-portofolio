'''
Source:

Author: Talha


'''
from flask import Flask,render_template, jsonify, request
import random
import json
import data as dt
import pandas as pd 


app  = Flask(__name__)
PORT = 3000

@app.route("/", methods=["GET","POST"])
def startpy():
    
    pnl_list = get_data()

    return render_template("date.html",pnl_list=pnl_list) 


def get_data():
    
    df = pd.read_csv('pnl.csv')

    pnl_list    = df['pnl'].tolist()

    return pnl_list

if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)
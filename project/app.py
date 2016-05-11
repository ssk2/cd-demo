from flask import Flask
from flask import render_template
import json
import requests
import urllib2

app = Flask(__name__)

def getExchangeRates():
    rates = []
    # response = urllib2.urlopen('http://api.fixer.io/latest')
    # data = response.read()
    # rdata = json.loads(data, parse_float=float)
    rates.append( 0.15 )
    rates.append( 0.25 )
    rates.append( 0.30 )
    rates.append( 0.20 )
    return rates

@app.route("/")
def index():
    getExchangeRates()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)

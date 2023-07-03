from statistics import variance
from flask import Flask, jsonify, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    response = requests.get("http://192.168.0.157/report")
    j1=json.loads(response.text)
    resp1="{:10.2f}".format(round(float(j1["power"]),2))
    
    response = requests.get("http://192.168.0.240/report")
    j2=json.loads(response.text)
    resp2="{:10.2f}".format(round(float(j2["power"]),2))
    
    return jsonify(response1=resp1, response2=resp2)
    #return render_template('index.html', response1=resp1, response2=resp2);   
        
if __name__ == '__main__':
    app.run(debug=True)
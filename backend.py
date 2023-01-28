from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory
import requests
import json
import random

#import functions
from calculus1.py import limits, derivatives, picone
from linAlg import RREFMatrix


app = Flask(__name__)

@app.route('/')
def send_home():
    return send_from_directory('static', 'math.html')

@app.route('/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        return  jsonify({'question': pickone()})

if __name__ == '__main__':
    app.run(debug=True)

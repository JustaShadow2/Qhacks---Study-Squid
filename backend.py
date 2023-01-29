from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory
import requests
import json
import random

#import functions
from calculus1 import limits, derivatives, pickone
from linAlg import NewMatrix
from woflram import getSteps, getAnswer

qID = { "id": 0 }
questions = {}

app = Flask(__name__)

def getQuestion(id):
    id = int(id)
    if id in questions: return questions[id]
    else: return

@app.route('/')
def send_home():
    return send_from_directory('static', 'math.html')

@app.route('/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

@app.route('/api/calc')
def api():
    picked = pickone()

    pickedID = qID["id"]
    questions[qID["id"]] = picked[1]
    qID["id"] += 1
    return { "question": picked[0], "id": pickedID }

@app.route('/api/linalg')
def apiLinAlg():
    matrix = NewMatrix()

@app.route('/api/list')
def list():
    return questions

@app.route('/api/solve', methods=['POST'])
def solve():
    data = request.json
    print(data)
    q = getQuestion(data["id"])
    if (not q): return "x"
    entered = data["answer"]
    key = "Q6XVVP-E4R2JPV6TH"
    print(q)
    print(entered)
    api = "http://api.wolframalpha.com/v1/result?appid=" + key + "&i=" + entered + "%3D" + q
    response = requests.get(api) 
    return response.text

@app.route('/api/steps/<path:id>')
def steps(id):
    q = getQuestion(id)
    if (not q): return "x"
    return json.loads(getSteps(q))

if __name__ == '__main__':
    app.run(debug=True)
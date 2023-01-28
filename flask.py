from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests
import json
import random

#import functions
from calculus1 import limits, derivatives
from linAlg import RREFMatrix


app = Flask(__name__)

@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        info = request.form['info']
        question = limits()
        return redirect(url_for('secondpage', info=info, question=question))
    else:
        return render_template('main.html')

@app.route('/secondpage/<info>/<question>', methods=['GET', 'POST'])
def secondpage(info, question):
    if request.method == 'POST':
        return redirect(url_for('main'))
    else:
        return render_template('secondpage.html', info=info, question=question)

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        return  jsonify({'question': limits()})

if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests
import json
app = Flask(__name__)

@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        info = request.form['info']
        return redirect(url_for('secondpage', info=info))
    else:
        return render_template('main.html')

@app.route('/secondpage/<info>', methods=['GET', 'POST'])
def secondpage(info):
    if request.method == 'POST':
        return redirect(url_for('main'))
    else:
        return render_template('secondpage.html', info=info)

if __name__ == '__main__':
    app.run(debug=True)
    


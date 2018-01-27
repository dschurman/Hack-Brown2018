#!flask/bin/python

import sys

from flask import Flask, render_template, jsonify, request, redirect, Response
import random, json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_add_numbers')
def worker():
    a = request.args.get('a')
    return jsonify(result=a)

if __name__ == '__main__':
    app.run()

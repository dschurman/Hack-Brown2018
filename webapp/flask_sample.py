<<<<<<< HEAD
from flask import Flask, render_template
=======
#!flask/bin/python

#import sys
from summ_util import summarize_text, get_keywords
from pdf_to_text import parse_my_pdf
from flask import Flask, render_template, jsonify, request, redirect, Response
#import random, json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_add_numbers')
def worker():
    a = request.args.get('a')
    #a = parse_my_pdf('geo_pdf.pdf')
    summ = summarize_text(a)
    keys = get_keywords(a)
    return jsonify(result=summ + '\n\nKeywords:\n' + keys)

@app.route('/pdf')
def pdf():
    p = request.args.get('p')
    try:
        text = parse_my_pdf(p)
        summ = summarize_text(text)
        keys = get_keywords(text)
        return jsonify(result=summ + '\n\nKeywords:\n' + keys)
    except:
        text = "Invalid filepath boi."
        return jsonify(result=text)

if __name__ == '__main__':
    app.run()

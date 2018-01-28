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
    b = request.args.get('b')
    c = request.args.get('c')
    #a = parse_my_pdf('geo_pdf.pdf')
    summ = summarize_text(a, word_count=int(b))
    keys = get_keywords(a, words=int(c))
    return jsonify(result=summ + '\n\nKeywords:\n' + keys)

@app.route('/pdf')
def pdf():
    import re
    p = request.args.get('p')
    p = re.sub(r'^.*\\', '', p);
    print(p + "**")
    try:
        text = parse_my_pdf(p)
        b = request.args.get('b')
    	c = request.args.get('c')
        summ = summarize_text(text, word_count=int(b))
        keys = get_keywords(text, words=int(c))
        return jsonify(result=summ + '\n\nKeywords:\n' + keys)
    except:
        text = "Invalid filepath boi."
        return jsonify(result=text)

if __name__ == '__main__':
    app.run()

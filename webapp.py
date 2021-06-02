import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/graph")
def render_graph():
    return render_template('graph.html')

if __name__ =="__main__":
    app.run(debug=False)

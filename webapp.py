from flask import Flask, request, Markup, render_template, flash, url_for
from flask import redirect
from flask import session
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('graph.html')

if __name__ =="__main__":
    app.run(debug=False)

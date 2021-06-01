from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/home")
def render_main():
    return render_template('graph.html')

if __name__ =="__main__":
    app.run(debug=False,port=54321)

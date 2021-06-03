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

@app.route("/response",methods=['GET','POST'])
def render_response():
    return render_template('response.html', points=format_graph_points(get_number_of_shootings()))

def get_number_of_shootings():
    female, male, gender_other = False, False, False
    if request.form.get('gender1'):
        female = True
    if request.form.get('gender2'):
        male = True
    if request.form.get('gender3'):
        gender_other = True
    asian, black, hispanic, native, white, other, unknown = False, False, False, False, False, False, False
    if request.form.get('race1'):
        asian = True
    if request.form.get('race2'):
        black = True
    if request.form.get('race3'):
        hispanic = True
    if request.form.get('race4'):
        native = True
    if request.form.get('race5'):
        white = True
    if request.form.get('race6'):
        other = True
    if request.form.get('race7'):
        unknown = True
    gun, knife, toy, unarmed, weapon_other = False, False, False, False, False
    if request.form.get('weapon1'):
        gun = True
    if request.form.get('weapon2'):
        knife = True
    if request.form.get('weapon3'):
        toy = True
    if request.form.get('weapon4'):
        unarmed = True
    if request.form.get('weapon5'):
        weapon_other = True
        
    print(native)    
    with open("police_shootings.json") as shootings_data:
        number_of_shootings = json.load(shootings_data)
    num_shootings = {}
    for num in number_of_shootings:
        if not(asian == False and num["Person"]["Race"]=="Asian") and not (black == False and num["Person"]["Race"]=="African American") and not (hispanic == False and num["Person"]["Race"]=="Hispanic") and not (native == False and num["Person"]["Race"]=="Native American") and not (white == False and num["Person"]["Race"]=="White") and not (other == False and num["Person"]["Race"]=="Other")and not (unknown == False and num["Person"]["Race"]=="Unkown"):
            if not(female == False and num["Person"]["Gender"]=="Female") and not (male == False and num["Person"]["Gender"]=="Male") and not (gender_other == False and num["Person"]["Gender"]=="Unknown"):
                if not(gun == False and num["Factors"]["Armed"]=="gun") and not(knife == False and num["Factors"]["Armed"]=="knife") and not(toy == False and num["Factors"]["Armed"]=="toy weapon") and not(unarmed == False and num["Factors"]["Armed"]=="unarmed ") and not(weapon_other == False and num["Factors"]["Armed"]=="other"):
                    if num["Incident"]["Date"]["Year"]+((num["Incident"]["Date"]["Month"])/12) in num_shootings:
                        num_shootings[num["Incident"]["Date"]["Year"]+((num["Incident"]["Date"]["Month"])/12)]=num_shootings[num["Incident"]["Date"]["Year"]+((num["Incident"]["Date"]["Month"])/12)] + 1
                    else:
                        num_shootings[num["Incident"]["Date"]["Year"]+((num["Incident"]["Date"]["Month"])/12)] = 1
    return num_shootings
    
def format_graph_points(data):
    graph_points = ""
    for key in data:
    #{ y: 450, x: 450 },
        graph_points = graph_points + '{ y: ' + str(data[key]) + ', x: ' + str(key) + ' }, '
    graph_points = graph_points[:-2]
    return graph_points

if __name__ =="__main__":
    app.run(debug=True)

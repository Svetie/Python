from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninja")
def ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("ninja.html", all_dojos = dojos)

@app.route("/create_ninja", methods=["POST"])
def new_ninja():
    data = {
        "fname" : request.form['fname'],
        "lname" : request.form['lname'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id']
    }

    ninja_id = Ninja.add_ninja(data)
    return redirect(f'dojos/{request.form["dojo_id"]}')

# @app.route("/all_ninjas")
# def show_ninjas():
#     ninjas = Ninja.get_all_ninjas()
#     return render_template("all_ninjas.html", all_ninjas = ninjas)
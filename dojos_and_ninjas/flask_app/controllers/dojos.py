from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo

@app.route("/dojos")
def index():
    #call the class method to get dojos
    dojos  = Dojo.get_all_dojos()
    print(dojos)
    return render_template("dojo.html", all_dojos = dojos)

@app.route("/new_dojo", methods=["POST"])
def add_dojo():
    data = {
        "dojo_name" : request.form["dojo_name"],
    }
    dojo_id = Dojo.save_dojo(data)
    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def show_dojo(id):
    data = {
        "dojo_id" : id
    }
    dojo =Dojo.get_ninjas_in_dojo(data)
    return render_template("dojo_show.html", dojo = dojo)
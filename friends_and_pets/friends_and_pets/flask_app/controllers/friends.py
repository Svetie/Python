from flask_app import app
from flask import render_template, redirect, request
# import the class from friend.py
from flask_app.models.friend import Friend

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all_friends()
    print(friends)
    return render_template("index.html", all_friends = friends)

# =======================================================
# SHOW ONE route
# =======================================================

@app.route("/<int:id>")
def one_friend(id):
    data = {
        "friend_id" : id
    }
    friend = Friend.get_pets_based_on_friend(data)
    print(friend)
    return render_template("show_one.html", friend = friend)

# =======================================================
# CREATE routes
# =======================================================

@app.route("/add_friend")
def add_friend():
    return render_template("new_friend.html")

@app.route('/create_friend', methods=["POST"])
def create_friend():

    if not Friend.validate_friend(request.form):
        return redirect("/add_friend")

    # set varchaar to 255 characters inside schema
    occupation_hash = bcrypt.generate_password_hash(request.form['occ'])
    print(occupation_hash)

    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : occupation_hash
    }
    # We pass the data dictionary into the save method from the Friend class.
    friend_id = Friend.save_friend(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

# =======================================================
# DELETE route
# =======================================================

@app.route("/delete/<int:id>")
def delete_friend(id):
    data = {
        "id" : id
    }
    Friend.delete_friend(data)
    return redirect("/")



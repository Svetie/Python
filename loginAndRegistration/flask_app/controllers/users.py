from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template('index.html')

#   Register

@app.route('/register', methods=['POST'])
def register():

    if not User.validate_registration(request.form):
        return redirect('/')

    # hash the password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    #if email already exists
    if User.get_user_by_email(data):
        flash('User with this email already exists')
        return redirect('/')

    # Call the save @classmethod on User
    user_id = User.save_user(data)
    user = User.get_user_by_email(data)
    # store user id into session
    session['user_id'] = user_id
    session['first_name'] = user.first_name
    # session['name'] = User.get_user_by_id(user_id)
    flash('You successfully registered')
    return redirect("/success")

# Login

@app.route('/login', methods = ['POST'])
def login():

    data = {
        'email' : request.form['email'],
    }
    user = User.get_user_by_email(data)

    #if email is not found
    if not user:
        flash('Invalid credentials')
        return redirect('/')

    # id password does not match
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid credentials')
        return redirect('/')

    # set id to session
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    flash('You successfully logged in')
    return redirect('/success')

@app.route('/success')
def success():

    if not 'user_id' in session:
        flash("Please login")
        return redirect('/')

    data = {
        "id" : session['user_id']
    }
    user = User.get_user_by_id(data)
    return render_template('success.html', user = user)

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out')
    return redirect('/')
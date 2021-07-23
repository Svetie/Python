from flask import flash
from flask_app import app
# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app.models.pet import Pet

# pipenv install flask-bcrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        # store related pets associated with an instance
        self.pets = []

    @staticmethod
    def validate_friend(data):
        is_valid = True
        if len(data['fname']) < 3:
            flash("First name must be at least 3 char")
            is_valid = False
        if len(data['lname']) < 3:
            flash("First name must be at least 2 char")
            is_valid = False
        if len(data['occ']) < 3:
            flash("First name must be at least 3 char")
            is_valid = False

        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!")
            is_valid = False

        return is_valid



    # Now we use class methods to query our database
    @classmethod
    def get_all_friends(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('friends_schema').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for one_record in results:
            friends.append( cls(one_record) )
        return friends
            
    @classmethod
    def get_one_friend(cls, data):
        query = "SELECT * FROM friends WHERE id = %(friend_id)s;"
        results = connectToMySQL('friends_schema').query_db(query, data)
        
        return cls( results[0] )
    
    @classmethod
    def save_friend(cls, data):
        query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW(), NOW());"

        id = connectToMySQL('friends_schema').query_db( query, data )
        
        return id

    @classmethod
    def get_pets_based_on_friend(cls, data):
        query = "SELECT * FROM friends LEFT JOIN pets ON pets.friend_id = friends.id WHERE friends.id = %(friend_id)s;"
        results = connectToMySQL('friends_schema').query_db(query, data)

        friend = cls( results[0] )

        for pet_info in results:
            pet_data = {
                "id" : pet_info['pets.id'],
                "name" : pet_info['name'],
                "age" : pet_info['age'],
                "friend_id" : pet_info['friend_id'],
                "created_at" : pet_info['pets.created_at'],
                "updated_at" : pet_info['pets.updated_at']
            }
            friend.pets.append( Pet(pet_data) )
        return friend

    @classmethod
    def delete_friend(cls, data):
        query = "DELETE FROM friends WHERE id = %(id)s;"
        results = connectToMySQL('friends_schema').query_db(query, data)
        return
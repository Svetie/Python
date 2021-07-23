# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the pet table from our database
class Pet:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.age = data['age']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_pet( cls , data ):
        query = "INSERT INTO pets ( name , age , friend_id, created_at , updated_at ) VALUES (%(name)s, %(age)s, %(friend_id)s, NOW(),NOW());"
        return connectToMySQL('friends_schema').query_db(query,data)
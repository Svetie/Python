from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # sabe a ninja

    @classmethod
    def save_ninja( cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, update_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, now(), now());"
        #returns id of new record
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

    @classmethod
    def add_ninja( cls, data ):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(age)s, %(dojo_id)s, now(), now());"
        id = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
        return id

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for one_record in results:
            ninjas.append( cls(one_record) )
        return ninjas

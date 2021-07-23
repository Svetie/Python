from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja import Ninja

#class Dojo
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #store ninjas in dojo
        self.ninjas = []

    # get all dojos
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        # results are returned as a list of dictionoaries
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        #list of dojos
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo))
        #return list of dojos
        return dojos

    # add new dojo
    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(dojo_name)s, NOW(), NOW());"
        id = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return id

    # get ninjas in dojo
    @classmethod
    def get_ninjas_in_dojo(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(dojo_id)s;"

        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        dojo = cls( results[0] ) # first dojo

        for ninja_data in results:
            ninja_data = {
                "id" : ninja_data["id"],
                "first_name" : ninja_data["first_name"],
                "last_name" : ninja_data["last_name"],
                "age" : ninja_data["age"],
                "dojo_id" : ninja_data["dojo_id"],
                "created_at" : ninja_data["created_at"],
                "updated_at" : ninja_data["updated_at"]
            }
            dojo.ninjas.append( Ninja(ninja_data))

        return dojo



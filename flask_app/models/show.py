from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Show:
    db = "user"
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.description = data['description']
        self.release_date = data['release_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO shows (title,network,description,release_date, users_id) VALUES(%(title)s,%(network)s,%(description)s,%(release_date)s,%(users_id)s)"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM shows;"
        results = connectToMySQL(cls.db).query_db(query)
        shows = []
        for row in results:
            shows.append( cls(row))
        return shows

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM shows WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE shows SET title=%(title)s, description=%(description)s, network=%(network)s, release_date=%(release_date)s, users_id=%(users_id)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @staticmethod
    def validate_show(shows):
        is_valid = True
        if len(shows['title']) < 3:
            flash("Title must be at least 3 characters","register")
            is_valid= False
        if len(shows['network']) < 3:
            flash("Network must be at least 3 characters","register")
            is_valid= False
        if len(shows['description']) < 8:
            flash("Description must be at least 8 characters","register")
            is_valid= False
        if shows['release_date'] == '':
            is_valid= False
            flash("Please enter a valid release date","register")
        return is_valid
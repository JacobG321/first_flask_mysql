# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    #how we display information
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        if len(results) == 0:
            return []
        else:
            friends = []
            # Iterate over the db results and create instances of friends with cls.
            for friend in results:
                friends.append( cls(friend) )
                #cls is place holder for Friend class, we are creating a friend object inside of the list
            return friends

    #this is how we add to the Database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(occupation)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('first_flask').query_db( query, data )
        #the s's are for string

    @classmethod
    def get_one_friend(cls, data):
        query = "SELECT * FROM friends WHERE id = %(id)s;"
        results = connectToMySQL('first_flask').query_db(query, data)
        if len(results) == 0:
            return None #can only return one item at most
        else:
            #create instance froma  dictionary at index 0 in the list of dictionaries called results
            return cls(results[0]) #need [0] because "results" is a list of dictionaries, but we a need a dictionary, which is at index 0

    @classmethod
    def edit_friend(cls, data):
        query = "UPDATE friends SET first_name = %(first_name)s, last_name = %(last_name)s, occupation = %(occupation)s WHERE id = %(id)s;"
        return connectToMySQL('first_flask').query_db(query, data)

    @classmethod
    def delete_friend(cls, data):
        query = "DELETE FROM friends WHERE id = %(id)s;"
        return connectToMySQL('first_flask').query_db(query, data)
from pymongo import MongoClient
from bson.objectid import ObjectId
from json import dumps

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username = "myUserAdmin", password = "1234"):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:32464' % (username, password))
        # where 32464 is the unique port number. "myUserAdmin" is the username, and "1234" is the password by default
        self.database = self.client['AAC']
        # AAC is the name of the database
        self.collection = self.database['animals']
        # animals is the name of the database
        
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        try:
            if type(data)==dict:
                self.collection.insert_one(data)  # data should be dictionary
                return True
            if type(data)==list:
                self.collection.insert_many(data)  # data should be list
                return True
            else:
                raise TypeError("Data must be formatted as dict or list")
        except Exception as e:
            #print(e)
            return False
        
    # Create method to implement the R in CRUD.
    def read(self, data):
        try:
            return(self.collection.find(data))
        except Exception as e:
            return str(e)
    
    # Delete method to implement the D in CRUD.
    def update(self, lookup_data, new_data):
        try:
            unformated_result = self.collection.update_many(lookup_data, new_data)
            dict_result = {}
            dict_result["acknowledged"] = unformated_result.acknowledged
            dict_result["matched_count"] = unformated_result.matched_count
            dict_result["modified_count"] = unformated_result.modified_count
            dict_result["raw_result"] = unformated_result.raw_result
            dict_result["upserted_id"] = unformated_result.upserted_id
            json_result = dumps(dict_result)
            return json_result
        except Exception as e:
            return str(e)
    
    # Delete method to implement the D in CRUD.
    def delete(self, data):
        try:
            unformated_result = self.collection.delete_many(data)
            dict_result = {}
            dict_result["acknowledged"] = unformated_result.acknowledged
            dict_result["deleted_count"] = unformated_result.deleted_count
            dict_result["raw_result"] = unformated_result.raw_result
            json_result = dumps(dict_result)
            return json_result
        except Exception as e:
            return str(e)

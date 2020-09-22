import pymongo

class MongoDB:
    """
    MongoDB class as an interface to connect MongoDB Atlas cloud
    with other Python scripts. Only one MongoDB instances per project
    """
    def __init__(self, connection_url, database_name, collection_name):
        client = pymongo.MongoClient(connection_url, ssl=True)
        db = client[database_name]
        self.collection = db[collection_name]

    def insert_single(self, dictionary):
        self.collection.insert_one(dictionary)

    def insert_mutiple(self, list_of_dict):
        self.collection.insert_many(list_of_dict)
    
    def find_by_criterion(self, criterion, value):
        return self.collection.find({criterion: value})

    def find_by_query(self, query_dict, projection_dict=None):
        return self.collection.find(query_dict, projection_dict)

class UniversityMongoDB(MongoDB):
    def get_school_names(self):
        list_of_all_schools = super().find_by_query({}, {"Name": 1})
        return [x for school_dict in list_of_all_schools for x in school_dict.values()] 


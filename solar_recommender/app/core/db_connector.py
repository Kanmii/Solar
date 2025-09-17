from pymongo import MongoClient

class MongoDBConnector:
    """
    Handles the connection to the MongoDB database.
    """
    def __init__(self, connection_string: str, db_name: str):
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        print(f"Connected to MongoDB database: {db_name}")

    def get_collection(self, collection_name: str):
        """
        Gets a specific collection from the database.
        """
        return self.db[collection_name]

    def save_data(self, collection_name: str, data: list):
        """
        Saves a list of dictionaries to a specified collection.
        """
        collection = self.get_collection(collection_name)
        # TODO: Implement bulk insert/update logic
        print(f"Saving {len(data)} documents to collection: {collection_name}")
        return True

# We can add other DB functions as needed

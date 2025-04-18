from AsunaRobot.modules.no_sql.users_db import *
from AsunaRobot.modules.no_sql.chats_db import *
from AsunaRobot.modules.no_sql.gban_db import *

from pymongo import MongoClient

from AsunaRobot import DB_NAME, DB_URI, LOGGER


# Client to connect to mongodb
mongodb_client = MongoClient(DB_URI)
if mongodb_client:
    LOGGER.info("Established connection to MongoDB!")

db = mongodb_client[DB_NAME]
if db:
    LOGGER.info(f"Connected to '{DB_NAME}' database")


class MongoDB:
    """Class for interacting with Bot database."""

    def __init__(self, collection) -> None:
        self.collection = db[collection]

    # Insert one entry into collection
    def insert_one(self, document):
        result = self.collection.insert_one(document)
        return repr(result.inserted_id)

    # Find one entry from collection
    def find_one(self, query):
        result = self.collection.find_one(query)
        if result:
            return result
        return False

    # Find entries from collection
    def find_all(self, query=None):
        if query is None:
            query = {}
        lst = []
        for document in self.collection.find(query):
            lst.append(document)
        return lst

    # Count entries from collection
    def count(self, query=None):
        if query is None:
            query = {}
        return self.collection.count_documents(query)

    # Delete entry/entries from collection
    def delete_one(self, query):
        self.collection.delete_many(query)
        after_delete = self.collection.count_documents({})
        return after_delete

    # Replace one entry in collection
    def replace(self, query, new_data):
        old = self.collection.find_one(query)
        _id = old["_id"]
        self.collection.replace_one({"_id": _id}, new_data)
        new = self.collection.find_one({"_id": _id})
        return old, new

    # Update one entry from collection
    def update(self, query, update):
        result = self.collection.update_one(query, {"$set": update})
        new_document = self.collection.find_one(query)
        return result.modified_count, new_document

    # Close connection
    @staticmethod
    def close():
        return mongodb_client.close()


def __connect_first():
    _ = MongoDB("test")
    LOGGER.info("Initialized Database!\n")


__connect_first()

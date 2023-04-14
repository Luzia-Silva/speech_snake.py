from app import app
from pymongo.mongo_client import MongoClient
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

if __name__ == "__main__":
    uri = os.environ.get("URI")
    client = MongoClient(uri)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        app.run()
    except Exception as e:
        print(e)

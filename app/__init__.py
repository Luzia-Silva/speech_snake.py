from flask import Flask
import os
from os.path import join, dirname
from dotenv import load_dotenv
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.config['SECRET_KEY']= os.environ.get("SECRET_KEY")
client = MongoClient(os.environ.get("DATABASE"))
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
from app.controllers import routes
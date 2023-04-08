from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']='d5fb8c4fa8bd46638dadc4e751e0d68d'

from app.controllers import routes
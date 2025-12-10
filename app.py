from flask import Flask
from database import db
import os
from dotenv import load_dotenv
from model.meal import Meal

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CONNECTION_DB')

db.init_app(app)


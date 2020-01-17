from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS,cross_origin
#Creating app and db objects
app = Flask(__name__)
cors=CORS(app)
# uri 'mysql://<username>:<password>@<host>:<port>/<dbname>'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:karizma5181@iotapplication.cdmmnd2zokfr.us-east-2.rds.amazonaws.com:3306/IOTApp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
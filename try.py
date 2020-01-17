'''from sqlalchemy import *
import sqlalchemy

conn_string="mysql://admin:karizma5181@iotapplication.cdmmnd2zokfr.us-east-2.rds.amazonaws.com:3306/iotapplication"
engine= sqlalchemy.create_engine(conn_string,echo=True)

#=db.engine.execute("Create table users (User_Id INT PRIMARY KEY AUTOINCREMENT,username VARCHAR(255) NOT NULL,password_hash VARCHAR(255) NOT NULL)")
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

#Creating app and db objects
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:karizma5181@iotapplication.cdmmnd2zokfr.us-east-2.rds.amazonaws.com:3306/iotapplication'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)'''

import pandas as pd
import pymysql

host="iotapplication.cdmmnd2zokfr.us-east-2.rds.amazonaws.com"
port=3306
dbname="IOTApp"
user="admin"
password="karizma5181"

conn = pymysql.connect(host, user=user,port=port,
                           passwd=password, db=dbname)
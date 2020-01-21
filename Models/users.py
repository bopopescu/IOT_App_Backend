from Utilities.config import db
from passlib.apps import custom_app_context as pwd_context

class User(db.Model):
    __tablename__ = 'users'
    User_Id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), index = True)
    password_hash = db.Column(db.String(128))

    #The hash_password() method takes a plain password as argument and stores a hash of it with the user. 
    # This method is called when a new user is added
    def hashPassword(self, password):
        self.password_hash = pwd_context.encrypt(password)

    #The verify_password() method takes a plain password as argument and returns True if the password is correct and false is not
    #This method is called whenever the user provides credentials and we need to verify them
    def verifyPassword(self, password):
        return pwd_context.verify(password, self.password_hash)

def addUser(data):
    username = data['username']
    password = data['password']
    #checking validity of entered username
    if username is None or password is None or username is "":
        return "Username or password is Null" # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        return "Username exists"
    user = User(username = username)
    user.hashPassword(password) 
    #making changes in the Database
    db.session.add(user)
    db.session.commit()
    return "User Added Successfully"

def verifyLogin(data):
    username = data['username']
    password = data['password']
    if username is "" or password is None:
        return "Username or password is missing" # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        user = User.query.filter_by(username=username).first()
        pass_entered=user.verifyPassword(password)
        if pass_entered==True:
            return "Login Successful"
        else:
            return "Wrong Password"
    else:
        return "User Not Found"
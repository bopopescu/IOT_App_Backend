from Utilities.config import app,db
from Models.users import *
from flask import request

@app.route('/RegisterUser',methods=['POST'])
def RegisterUser():
    data=request.json
    result=addUser(data)
    
    return result

if __name__ == "__main__":
    app.run(port=5001, debug=True)

from Utilities.config import app,db
from Models.users import *
from flask import request

@app.route('/login',methods=['POST'])
def LoginUser():
    data=request.json
    result=verifyLogin(data)
    
    return result

if __name__ == "__main__":
    app.run(port=5000, debug=True)

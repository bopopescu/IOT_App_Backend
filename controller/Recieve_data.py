from Utilities.config import app,db
from Models.data import *
from flask import request

@app.route('/data',methods=['POST'])
def Receive():
    data=request.json
    result=receiveData(data)
    return result

if __name__ == "__main__":
    app.run(port=5002, debug=True)
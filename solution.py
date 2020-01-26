import mysql.connector
from flask import Flask, jsonify, request 
import json

"""
DB Structure

empID
directSuperiorID
An employee with directSuperiorID as itself has no superior

"""

app = Flask(__name__) 

@app.route('/', methods = ['GET']) 
def disp(): 
    empID = request.args.get('id')
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database = "pytest")
    mycursor = mydb.cursor()
    
    sql = "Select * from user"
    mycursor.execute(sql)
    alldata = mycursor.fetchall()

    empID=int(empID)
    ids = {}
    for row in alldata:
        ids[int(row[0])]=int(row[1])
        print(row[0],"  ",row[1])
    res = []
    while empID!=ids[empID]:
        print(empID)
        res.append(empID)
        empID=ids[empID]
    res.append(empID)
    res.reverse()
    res = json.dumps({'hierarchy': res})
    return res 


if __name__ == '__main__': 
  
    app.run(debug = True)
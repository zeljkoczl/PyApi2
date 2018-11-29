import flask
import json
from flask import request, jsonify
import flask_api
from flask_api import status

token = '123'

employees = {
  "employees": {
         "names": ['a', 'b', 'c']
         }
}
                   
departments = {
    "departments": ['a', 'b', 'c'] 
}

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/employees", methods=['GET', 'POST'])
def employees_api():
  print(request.headers['token'])
  if request.headers['token'] == token:
        if request.method == 'GET':
              return jsonify(employees)
        elif request.method == 'POST':
              name = request.args['name']
              employees['employees']['names'].append(name)
              return jsonify(employees)      
        else:
              return '', status.HTTP_405_METHOD_NOT_ALLOWED
  else: 
   return '', status.HTTP_401_UNAUTHORIZED

@app.route("/departments", methods=['GET', 'POST'])
def departments_api():
  print(request.headers['token'])
  if request.headers['token'] == token:
        if request.method == 'GET':
              return jsonify(departments)
        elif  request.method == 'POST':
              name = request.args['departments']
              departments['departments'].append(name)
              return jsonify(departments)
        else:
              return '', status.HTTP_405_METHOD_NOT_ALLOWED
  else:
   return '', status.HTTP_401_UNAUTHORIZED

@app.errorhandler(404)
def other():
    return '', status.HTTP_403_FORBIDDEN

app.run()



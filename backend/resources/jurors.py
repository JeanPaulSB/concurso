from flask import Response,request,jsonify
from flask_restful import Resource
from database.db import client
from bson import json_util, ObjectId

import json

db = client.Users
collection = db.jurors

class Register(Resource):
    # registering a juror
    def post(self):

        obj = {}

        # getting juror's data
        name = request.form["name"]
        lastName = request.form["lastName"]
        email = request.form["email"]
        #upb_id = request.form["upb_id"]
        #password = request.form["password"]


        obj["name"] = name
        obj["lastName"] = lastName
        obj["email"] = email
        obj["participants"] = []
        #obj["upb_id"] = upb_id
        #obj["password"] = password
        
        # checking if user is already registered
        jurors = collection.find_one({'email':email})
        if not jurors:
            # registering user
            collection.insert_one(obj)
            return 201
            
        
        # user is already registered
        return 404

    def get(self):
        print(client)
        return "nice"
    
class Juror(Resource):
    
    
    def get(self,upb):
        # returns all the jurors
        juror = list(collection.find({'upb_id':upb}))

        return json.loads(json_util.dumps(juror))

class Jurors(Resource):
    def get(self):
        jurors = list(collection.find({}))
        return json.loads(json_util.dumps(jurors))

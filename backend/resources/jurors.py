from flask import Response,request,jsonify
from flask_restful import Resource
from database.db import client
from database.utils import *
from bson import json_util, ObjectId




import json
import pandas as pd
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
        upb_id = request.form["upb_id"]
        password = request.form["password"]
        row_id = request.form["row_id"]


        obj["name"] = name
        obj["lastName"] = lastName
        obj["email"] = email
        obj["participants"] = []
        obj["upb_id"] = upb_id
        obj["password"] = password
        obj["row_id"] = row_id
        
        # checking if user is already registered
        jurors = collection.find_one({'email':email})
        print(jurors)
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

class Login(Resource):
    def post(self):
        email = request.form["email"]
        password = request.form["password"]

        juror = list(collection.find({'email':email}))
        
        if juror:
            # checking if the indicated password matches the required one
            if juror[0]["password"] == password:
                
                return Response(
                    response = json.dumps({"data":{
                        "message":"success",
                        "name":juror[0]["name"],
                        "email":juror[0]["email"],
                        "id":juror[0]["upb_id"],
                        "isAdmin":juror[0]['isAdmin'],
                        "seccional": juror[0]["seccional"],
                    }}),
                    status = 201,
                    mimetype = "application/json"
                )
            else:
                return Response(
                    response = json.dumps({"data":{
                        "message":"Contraseña incorrecta"
                    }}),
                    status = 201,
                    mimetype = "application/json"
                )


        else:
           return Response(
            response = json.dumps({"data":{
                "message":"Email no encontrado!"
            }}),
            status = 201,
            mimetype = "application/json"
           )
        print(juror)

class History(Resource):
    
    def post(self):
        # TODO: add exceptions
        upb_id = int(request.form["upb_id"])
        records = getHistory(upb_id)
        return json.loads(json_util.dumps(records))

class Revert(Resource):
    
    def post(self):
        participant_id = request.form["participant_id"]
        time = request.form["time"]
        revertDowngrade(participant_id,time)
        return 201

class JurorsParticipants(Resource):
    
    def get(self):
        jurors = list(collection.find({}))
        
        for juror in jurors:
            print(juror.keys())
            juror_id = juror['upb_id']
            result = getParticipants(juror_id)
            juror['participants'] = result
            
        return json.loads(json_util.dumps(jurors))

class JurorByParticipant(Resource):

    def post(self):
        participant_id = request.form["participant_id"]
        
        return json.loads(json_util.dumps(getJuror(participant_id)))
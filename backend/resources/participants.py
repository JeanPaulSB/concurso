from flask import Response,request,jsonify,send_from_directory,send_file
from flask_restful import Resource
from database.db import client
from bson import json_util, ObjectId
from database.utils import getJuror



import random
import json
import pandas as pd
import numpy as np

db = client.Users
collection = db.participants

class LoadParticipants(Resource):
    def post(self):
        if len(request.files) > 0:
            print("recieving file")
            # validating that the file is actually being sended
            data = request.files['file']
            extension = data.filename.split('.')[1]
            # ensuring that we are reading and excel file
            if not extension in ['xlsx','xlsm']:
                return 404
            
            try:
                excel_file = pd.read_excel(data)
                # traversing excel sheet records
                count = 0
                for index,row in excel_file.iterrows():

                    # fields that we need to register [ID,Nombre,ID (Incluyendo los ceros),Seleccione la seccional de la Universidad en la que actualmente estudia]
                    obj = {}
                    name = row['Nombre']
                    upb_id = row['ID (Incluyendo los ceros)']
                    row_id = row['ID']
                    seccional = row['Seleccione la seccional de la Universidad en la que actualmente estudia']

                    obj["name"] = name
                    obj['row_id'] = row_id
                    obj['seccional'] = seccional
                    obj["wrongQuestions"] = 0
                    obj["upb_id"] = upb_id

                    count = index

                    
                    collection.insert_one(obj)
                    
                print("file sended, nice")
                return Response(
                    response = json.dumps({"data" : {
                        "message": "success",
                        "registered_users": count+1
                    }}),
                    status = 201,
                    mimetype = "application/json"
                )
            except Exception as e:
                print(str(e))
                return Response(json.dumps({"data":{
                    "message":"something went wrong"
                }}),status = 404, mimetype = "application/json")
            

class Assign(Resource):
    def get(self):

        # NOTE: MEDELLIN SECCIONAL
        # getting participants ids
        participants = [elem['_id'] for elem in list(collection.find({'seccional':'Medellín'}))]
        # accessing jurors db and getting all the participants as 2d array with chunks of 3 elements
        jurors = db.jurors
        participants = list(chunks(participants,3))
        
        # listing  jurors
        jurors_list = list(jurors.find({'seccional':'Medellín'}))
        for juror in jurors_list:
            # getting random chunk from the main list of participants
            # and assigning it to a juror
            if len(participants) > 0:
                participants_choice = random.choice(participants)
            
                juror_id = juror['_id']
                # update the corresponding record
                jurors.update_one({'_id':juror_id},{"$set":{"participants":participants_choice}})
                # removing participant from the main list since it was alreayd selected
                participants.remove(participants_choice)

        # NOTE: BUCARAMANGA SECCIONAL


class Participants(Resource):
    def get(self):
        participants = list(collection.find({}))
        return json.loads(json_util.dumps(participants))

class Participant(Resource):
    def get(self,participant_id):
        
        participant = collection.find_one({'_id': ObjectId(participant_id)})
        if participant:
            return json.loads(json_util.dumps(participant))
        return "bad"
       


class GenerateReport(Resource):
    def get(self):
        participants = list(collection.find({}))
        new_participants = []
        jurors_collection = db.jurors

        for participant in participants:
            p_id = participant['_id']
            juror = getJuror(p_id)

    
            name = juror["name"]  if juror else None
            email = juror["email"]  if juror else None
            seccional = juror["seccional"] if juror else None
            upb_id = juror["upb_id"] if juror else None
                
            participant['juror_name'] = name
            participant['juror_email'] = email
            participant['juror_seccional'] = seccional
            participant['juror_upbid'] = upb_id
                
                
            
            new_participants.append(participant)

        result = pd.json_normalize(json.loads(json_util.dumps(new_participants)),max_level = 2)

        result.to_excel('resultados.xlsx')

        return send_file(filename = "resultados.resultados.xlsx")


"""
splits list into chunks of 3 elements and returns 2d array
"""
def chunks(participants: list,n:int):
    for i in range(0,len(participants),n):
        yield participants[i:i+n]
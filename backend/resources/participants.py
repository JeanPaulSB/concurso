from flask import Response,request,jsonify
from flask_restful import Resource
from database.db import client
from bson import json_util, ObjectId




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
            
            excel_file = pd.read_excel(data)
            # traversing excel sheet records
            for index,row in excel_file.iterrows():

                # fields that we need to register [ID,Nombre,ID (Incluyendo los ceros),Seleccione la seccional de la Universidad en la que actualmente estudia]
                obj = {}
                name = row['Nombre']
                upb_id = row['ID (Incluyendo los ceros)']
                row_id = row['ID']
                seccional = ['Seleccione la seccional de la Universidad en la que actualmente estudia']
                obj["name"] = name
                obj['row_id'] = row_id
                obj['seccional'] = seccional
                obj['questions'] = []
                obj["wrongQuestions"] = 0


                
                collection.insert_one(obj)
                
            print("file sended, nice")
        return 200

class Assign(Resource):
    def get(self):
        # getting participants ids
        participants = [elem['_id'] for elem in list(collection.find({}))]
        # accessing jurors db and getting all the participants as 2d array with chunks of 3 elements
        jurors = db.jurors
        participants = list(chunks(participants,3))
        
        # listing  jurors
        jurors_list = list(jurors.find({}))
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
       



"""
splits list into chunks of 3 elements and returns 2d array
"""
def chunks(participants: list,n:int):
    for i in range(0,len(participants),n):
        yield participants[i:i+n]
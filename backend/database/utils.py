"""
Function that returns current participants for a juror 
"""
from .db import client
from bson import ObjectId,json_util

db = client.Users
"""
Function that recieves a juror_id and returns its corresponding participants
"""
def getParticipants(juror_id: int) -> list:
   
    collection = db.jurors
    result = collection.find_one({'upb_id':juror_id})['participants']
    
    # storing participants
    participants = []
    for participant in result:
        collection = db.participants
        query = collection.find_one({'_id': ObjectId(participant)})
        participants.append(query)
    return participants

"""
Function intended to mark a particpant's answer as wrong
"""
def downvoteParticipant(participant_id: str) -> list:
    collection = db.participants

    # getting participant
    participant = collection.find_one({'_id':ObjectId(participant_id)})

    questions_failed = participant['questions_failed']
    questions_failed += 1

    # updating record
    collection.update_one({'_id':ObjectId(participant_id)},{"$set":{"questions_failed": questions_failed}})



def revertDowngrade(participant_id: str):
    collection = db.participants

    # getting participant
    participant = collection.find_one({'_id':ObjectId(participant_id)})

    questions_failed = participant['questions_failed']
    questions_failed -= 1

    # updating record
    collection.update_one({'_id':ObjectId(participant_id)},{"$set":{"questions_failed": questions_failed}})


def recordTransaction(data: dict):
    collection = db.history
    collection.insert_one(data)
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
    print(participant_id)
    # getting participant
    participant = collection.find_one({'_id':ObjectId(participant_id)})

    questions_failed = participant['wrongQuestions']
    questions_failed += 1

    # updating record
    collection.update_one({'_id':ObjectId(participant_id)},{"$set":{"wrongQuestions": questions_failed}})



def revertDowngrade(participant_id: str,time: str):
    collection = db.participants

    participant_id = str(participant_id)
    print(participant_id)
    # getting participant
    participant = collection.find_one({'_id':ObjectId(participant_id)})


    questions_failed = participant['wrongQuestions']
    if questions_failed > 0:
        questions_failed -= 1

    history_collection = db.history
    history_collection.delete_one({'time':time})
    print(time)
    # updating record
    collection.update_one({'_id':ObjectId(participant_id)},{"$set":{"wrongQuestions": questions_failed}})


def recordTransaction(data: dict):
    collection = db.history
    collection.insert_one(data)

"""
Function that returns all the transactions from a user
"""
def getHistory(juror_id: int) -> list:
    collection = db.history
    records = list(collection.find({'juror':juror_id}))
    return records

def getParticipantsHistory(participant_id: str) -> list:
    collection = db.history
    print(participant_id)
    records = list(collection.find({'participant_id':participant_id}))
    return records

"""
Function that returns a Juror for the corresponding partcipant
"""
def getJuror(participant_id: str) -> str:
    collection = db.jurors
    juror = collection.find_one({'participants': ObjectId(participant_id) })

    return juror
    

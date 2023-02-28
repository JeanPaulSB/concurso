from flask import Flask
from flask_restful import Resource,Api
from flask_cors import CORS
from flask_socketio import SocketIO,send,emit,join_room,leave_room
from bson import ObjectId,json_util
from threading import Lock
from werkzeug.middleware.proxy_fix import ProxyFix


# importing resources
from resources.jurors import Register,Juror,Jurors,Login
from resources.participants import LoadParticipants,Assign,Participants,Participant
from database.db import client
from database.utils import getParticipants,downvoteParticipant,recordTransaction

import json
import logging


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)

app.wsgi_app = ProxyFix(app.wsgi_app,x_for=1,x_proto=1)
socketio = SocketIO(app,logger = True,engineio_logger = True, async_mode = "gevent")

# creating thread
thread = None
thread_lock = Lock()

# accessing our db
db = client.Users
    



api.add_resource(Register,"/api/juror/register")
api.add_resource(Juror,"/api/jurors/<int:upb>")
api.add_resource(Jurors,"/api/jurors/list")
api.add_resource(Login,"/api/login")
api.add_resource(LoadParticipants,"/api/participants/register")
api.add_resource(Assign,"/api/participants/assign")
api.add_resource(Participants,"/api/participants/list")
api.add_resource(Participant,"/api/participant/<participant_id>")

rooms = []

def background_thread():
    while True:
        socketio.sleep(1)
        collection = db.participants
        for room in rooms:
            participants = json.loads(json_util.dumps(getParticipants(room)))
            print(f"getting participants for {room}")
            socketio.emit('participants',participants,to = room)




@socketio.on('join')
def logged(data):
    room = data['room']
    join_room(room)
    rooms.append(room)
    print(f"added room {room}")
    global thread
    with thread_lock:
            if thread is None:
                thread = socketio.start_background_task(background_thread)
    emit('my_response','connected')
    print("user connected")

@socketio.on('leave')
def leave(data):
    room = data['room']
    print(f"user {room} is leaving its room")
    leave_room(room)
    print(rooms)
    rooms.remove(room)
    print(rooms)

    

@socketio.on('downvote')
def downvote(data):
    id = data['participant_id']
    downvoteParticipant(id)
    recordTransaction(data)
    print(f"downvoted {id}")




if __name__ == "__main__":
    print("running app...")
    socketio.run(app,host = '0.0.0.0',debug = True)



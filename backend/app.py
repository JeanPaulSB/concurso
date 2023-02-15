from flask import Flask
from flask_restful import Resource,Api
from flask_cors import CORS
from flask_socketio import SocketIO,send,emit
# importing resources
from resources.jurors import Register,Juror,Jurors,Login
from resources.participants import LoadParticipants,Assign,Participants,Participant



app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app,logger = True)




api.add_resource(Register,"/api/juror/register")
api.add_resource(Juror,"/api/jurors/<int:upb>")
api.add_resource(Jurors,"/api/jurors/list")
api.add_resource(Login,"/api/login")
api.add_resource(LoadParticipants,"/api/participants/register")
api.add_resource(Assign,"/api/participants/assign")
api.add_resource(Participants,"/api/participants/list")
api.add_resource(Participant,"/api/participant/<participant_id>")

@socketio.on('message')
def handle_message(message):
    print(message)
    send("dale rey la buena")
    





if __name__ == "__main__":
    print("running app...")
    socketio.run(app,host = '0.0.0.0')



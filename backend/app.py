from flask import Flask
from flask_restful import Resource,Api
from flask_cors import CORS
# importing resources
from resources.jurors import Register,Juror,Jurors,Login
from resources.participants import LoadParticipants,Assign,Participants,Participant



app = Flask(__name__)
api = Api(app)
CORS(app)




api.add_resource(Register,"/jurors/register")
api.add_resource(Juror,"/jurors/<int:upb>")
api.add_resource(Jurors,"/jurors/list")
api.add_resource(Login,"/api/login")
api.add_resource(LoadParticipants,"/participants/register")
api.add_resource(Assign,"/participants/assign")
api.add_resource(Participants,"/participants/list")
api.add_resource(Participant,"/participant/<participant_id>")






if __name__ == "__main__":
    app.run(debug = True)



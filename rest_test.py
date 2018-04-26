from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username == "admin" and password == "password":
        return True
    return False

class EventsByIdentity(Resource):
    @auth.login_required    
    def get(self, identity_id):
        try:
            identity_int = int(identity_id)
        except:
            #raise InvalidUsage('ID is not string', status_code=400)
            return {},400
        data = { 12: [ { "time": "04-25-2018T00:00:00Z", "class": 2 },
                       { "time": "04-25-2018T01:00:00Z", "class": 5 } ] }
        if identity_int not in data:
            return {},200
        return data[identity_int]

api.add_resource(EventsByIdentity, '/v1/identities/<identity_id>/events')

if __name__ == "__main__":
    app.run(port=5001, host='0.0.0.0', ssl_context='adhoc')

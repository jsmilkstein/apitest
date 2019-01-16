#!/usr/bin/env python
import random
from flask import Flask, request
#from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

#auth = HTTPBasicAuth()

class Agent(Resource):
    def get(self):
        r = random.randint(1,100)
        if r < 80:
            return {"Message":"Good checkin"},200
        elif r < 90:
            return {"Message":"Bad request"},400
        return {"Message":"Server error"},500

api.add_resource(Agent, '/v1/checkin')

if __name__ == "__main__":
    app.run(port=5001, host='0.0.0.0')

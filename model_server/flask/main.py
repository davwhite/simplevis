#!/usr/bin/env python3.8
from flask import Flask
from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
from waitress import serve, logging

from functions.model_functions import *

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

class Detect(Resource):
    def get(self):
        x = detect()
        return jsonify(x)

api.add_resource(Detect,'/detect')

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)

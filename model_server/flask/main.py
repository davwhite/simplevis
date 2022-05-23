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


##
## Actually setup the Api resource routing here
##
api.add_resource(Detect,'/detect')


# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    #We now use this syntax to server our app. 
    serve(app, host='0.0.0.0', port=5000)

# @app.route('/')
# def hello_world():
#     msg = "Welcome to FuncFlasker"
#     if request.method == 'GET':
#         return msg
#     else:
#         return msg

# @app.route('/panel_details/<panel_id>', methods=['GET'])
# def panelfunctions_panel_details():
#     # panel_id = request.args.get('panel_id','N/A')
#     x = panel_details(panel_id)
#     return x
# @app.route('/panel_statements', methods=['GET'])
# def panelfunctions_panel_statements():
#     panel_id = request.args.get('panel_id','N/A')
#     statement_type = request.args.get('statement_type','N/A')
#     speaker = request.args.get('speaker','N/A')
#     x = panel_statements(panel_id, statement_type, speaker)
#     return x
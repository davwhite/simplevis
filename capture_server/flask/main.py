#!/usr/bin/env python3.8
from flask import Flask
from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
from waitress import serve, logging

from functions.capture_functions import *

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

class Test(Resource):
    def get(self):
        x = test()
        return jsonify(x)

class Capture(Resource):
    def get(self):
        x = capture()
        return jsonify(x)

# class PanelStatements(Resource):
#     def get(self, panel_id):
#         statement_type = 'N/A'
#         speaker = 'N/A'
#         x = panel_statements(panel_id,statement_type,speaker)
#         return jsonify(x)

# class PanelStatementTypes(Resource):
#     def get(self, statement_type):
#         panel_id = 'N/A'
#         speaker = 'N/A'
#         x = panel_statements(panel_id,statement_type,speaker)
#         return jsonify(x)

# class PanelStatementSpeaker(Resource):
#     def get(self, speaker):
#         panel_id = 'N/A'
#         statement_type = 'N/A'
#         x = panel_statements(panel_id,statement_type,speaker)
#         return jsonify(x)

# class PanelSearch(Resource):
#     def get(self, searchstring):
#         x = panel_search(searchstring)
#         return jsonify(x)

##
## Actually setup the Api resource routing here
##
api.add_resource(Test,'/test')
api.add_resource(Capture,'/capture')
# api.add_resource(Panel,'/panel_details/<panel_id>')
# api.add_resource(PanelStatements,'/panel_statements/<panel_id>')
# api.add_resource(PanelStatementTypes,'/panel_statements/type/<statement_type>')
# api.add_resource(PanelStatementSpeaker,'/panel_statements/speaker/<speaker>')
# api.add_resource(PanelSearch,'/panel_search/<searchstring>')


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
import json
import os
import cv2
from datetime import datetime

# config = {
#   'user': os.environ.get('DB_USER'),
#   'password': os.environ.get('DB_PWD'),
#   'host': os.environ.get('DB_HOST'),
#   'database': os.environ.get('DB_NAME'),
#   'raise_on_warnings': True
# }


def test():
  jsondata = ['this is a test']
  return jsondata

def capture():

  now = datetime.now() # current date and time
  date_time = now.strftime("%Y%m%d-%H%M%S")
  filepath = os.getenv('CAPTURE_PATH')
  nexus_user = os.getenv('NEXUS_USER')
  nexus_pass = os.getenv('NEXUS_PASS')
  nexus_url = os.getenv('NEXUS_URL')
  ipath = filepath
  impath = filepath+'/image-'+date_time+'.jpg'
  imname = impath
  cap = cv2.VideoCapture(0)

  # Capture frame
  ret, frame = cap.read()
  if ret:
    cv2.imwrite(imname, frame)
  cap.release()

  curlcmd = "curl -v -u "+nexus_user+":"+nexus_pass+" --upload-file "+impath+" "+nexus_url+"/repository/simplevis-artifacts/incoming/"
  curler = curlcmd
  stream = os.popen(curler)
  output = stream.read
  # print(output)
  jsondata = ['captured']
  return jsondata


# def panel_statements(panel_id, statement_type, speaker):
#   if panel_id != "N/A":
#     query = ("select statement,speaker,statement_time,statement_type from panel_statements where panel_id = '" + panel_id + "'")
#   elif statement_type != "N/A":
#     query = ("select a.panel_id,b.panel_title,a.speaker,a.statement,a.statement_time,a.statement_type from panel_statements a, panel_details b where a.panel_id=b.panel_id and a.statement_type = '" + statement_type + "'")
#   elif speaker != "N/A":
#     query = ("select a.panel_id,b.panel_title,a.speaker,a.statement,a.statement_time,a.statement_type from panel_statements a, panel_details b where a.panel_id=b.panel_id and a.speaker = '" + speaker + "'")
#   jsondata = get_query_results(query)
#   return jsondata

# def panel_search(searchstring):
#   query = ("select a.panel_id, b.panel_title, a.statement, a.speaker, a.statement_time, a.statement_type from panel_statements a, panel_details b where a.panel_id=b.panel_id and match(a.statement) against ('" + searchstring +"' in natural language mode)")
#   jsondata = get_query_results(query)
#   return jsondata
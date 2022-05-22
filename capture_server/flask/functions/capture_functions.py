import json
import os
import cv2

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
  filepath = os.getenv('CAPTURE_PATH')
  nexus_user = os.getenv('NEXUS_USER')
  nexus_pass = os.getenv('NEXUS_PASS')
  ipath = ''.join(filepath)
  impath = filepath,'/image.jpg'
  imname = ''.join(impath)
  cap = cv2.VideoCapture(0)

  # Capture frame
  ret, frame = cap.read()
  if ret:
    cv2.imwrite(imname, frame)
  cap.release()

  # Upload captured image
  curl_request = 'curl -v -u admin:admin123 --upload-file ',imname,' http://nexus-service-nexus.apps.ocp4.davenet.local/repository/simplevis-artifacts/capture/image.jpg'
  creq = ''.join(curl_request)
  result = os.popen(creq)
  output = result.read()

  jsondata = [output]
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
import json
import os
import cv2
from datetime import datetime

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
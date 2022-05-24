import json
import os
import shutil
import requests
import glob
import subprocess

def detect():
  nexus_user = os.getenv('NEXUS_USER')
  nexus_pass = os.getenv('NEXUS_PASS')
  nexus_url = os.getenv('NEXUS_URL')
  yolodir = os.getenv('YOLODIR')

  params = dict(
      repository='simplevis-artifacts'
  )

  
  search_url = nexus_url+"/service/rest/v1/search"
  surl = search_url
  print(surl)
  resp = requests.get(url=surl, params=params)
  data = resp.json() # Check the JSON Response Content documentation below
  jsondata = []
  item_dict = data
  # print(len(item_dict['items']))
  for rec in data['items']:
    for dl in rec['assets']:
      # print(dl['downloadUrl'])
      id = dl['id']
      path = dl['path']
      isincoming = path.find('incoming')
      if isincoming >=0:
        durl = dl['downloadUrl']
        imgrec = {'id': id,'path': path, 'url': durl}
        jsondata.append(imgrec)

 
  # Create directory if it's not there
  ddir = yolodir+'/incoming'
  ydir = ddir
  if not os.path.exists(ydir):
    os.makedirs(ydir)

  # # Download all the images
  ifiles = []
  for img in jsondata:
    url = img['url']
    nam = img['path']
    r = requests.get(url, allow_redirects=True)
    ifile = yolodir+"/"+nam
    fname = ifile
    # print(fname)
    open(fname, 'wb').write(r.content)
    ifiles.append(fname)

  # # TODO replace curl with requests
  for ifile in ifiles:
    curlcmd = "curl -v -u "+nexus_user+":"+nexus_pass+" --upload-file "+ifile+" "+nexus_url+"/repository/simplevis-artifacts/captured/"
    curler = curlcmd
    # print(curler)
    stream = os.popen(curler)
    output = stream.read
    # print(output)

  # # Delete downloaded captures from nexus
  # for aid in jsondata:
  #   delete_url = nexus_url+"/service/rest/v1/assets/"+aid['id']
  #   durl = delete_url
  #   resp = requests.delete(url=durl,auth = (nexus_user, nexus_pass))
  #   print(resp)

  # Detect from uploaded images
  my_env = os.environ.copy()
  my_env["YOLODIR"] = yolodir
  # subprocess.Popen(my_command, env=my_env)
  for cfile in ifiles:
    dcommand = 'python '+yolodir+'/detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source '+cfile
    os.wait()
    process = os.popen(dcommand)
    os.wait()


  # # Delete incoming files. TODO only delete when successful
  # if os.path.exists(yolodir+"/incoming"):
  #   shutil.rmtree(yolodir+"/incoming")

  # Gather all the processed files
  exfiles = glob.glob(yolodir+"/runs/detect/exp*/*.jpg")
  
  # TODO replace curl with requests
  # Upload detection results
  for xfile in exfiles:
    curlcmd = "curl -v -u "+nexus_user+":"+nexus_pass+" --upload-file "+xfile+" "+nexus_url+"/repository/simplevis-artifacts/detected/"
    xStream = os.popen(curlcmd)
    xOutput = xStream.read
    print(xOutput)

  # # Delete detected files. TODO only delete when successful
  # if os.path.exists(yolodir+"/runs"):
  #   shutil.rmtree(yolodir+"/runs")


  return ['imdone']

# simple vision
Simple sample computer vision demo for edge devices. This sample application is built around the yolov5 pre-trained model for object detection in a image and/or video. 

## Release 1.1.0
- Updated README.md
- Added upload alternative for image capture

## Release 1.0.9
- Added simple webserver for model operation

## Release 1.0.8
- Added combined container with capture and detect.

## Release 1.0.7
- Removed output to Nexus
- Added write to staged folders on mount point
- Remove incoming and exp files when processed

## Release 1.0.6
- Added container build scripts

## Release 1.0.5 
- Uploads model detection output to Nexus
- Reorganized Dockerfiles for capture and model containers

## Release 1.0.3
- Runs multiple input files

## TODO
- Organize README.md file
- Create deployment for model container for OpenShift



## Running the capture container in podman
To enable access to an attached camera, the container must be launched with the "device" argument.
```
podman run -d --name <capturepodname> -p <captureport> --device /dev/video0 -v /data/simplevis:/data/simplevis <capture_image>
podman run -d --name simplevis -p 5000:5000 --device /dev/video0 -v simplevis:/data/simplevis simplevis
podman run -d --name web-serv -p 5005:5000 -v simplevis:/opt/app-root/src/flask/static web-serv
```

## When developing locally set the following environment variables before launching the flask app.
```
export FLASK_APP=flask/main.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export CAPTURE_PATH=<where your capture files will be created>
export NEXUS_USER=<username>
export NEXUS_PASS=<user password>
export NEXUS_URL=<base url for nexus>
export YOLODIR=<directory where yolov5 is cloned>
```
```
python flask/main.py
```

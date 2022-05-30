# simple vision
Simple sample computer vision demo for edge devices. This sample application is built around the yolov5 pre-trained model for object detection in a image and/or video. 

## Release 1.1.2.1
- Changed ports for apps
- Updated instructions to deploy in a pod
- Changed default connection for webserver to pod

## Release 1.1.2
- Updated model dockerfile
- Updated combined server dockerfile
- Updated readme
- Create incoming if not exist
- OCP deployment
- Added upload creation when directory not found

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

podman pod create -n simplevis -p 5001:5001 -p 5005:5005 --device /dev/video0

podman run -d \
--name simplevis-full \
-v simplevis:/data/simplevis \
--pod simplevis \
simplevis-full:1.1.2.1

podman run -d \
--name simplevis-web \
-v simplevis:/opt/app-root/src/flask/static \
--pod simplevis \
simplevis-web:1.1.2.1

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

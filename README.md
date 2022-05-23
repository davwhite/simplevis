```
podman build -t simplevision .
podman run -it --rm --device /dev/video0 simplevision
```

export FLASK_APP=flask/main.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export CAPTURE_PATH=/tmp
export NEXUS_USER=admin
export NEXUS_PASS=admin123
export NEXUS_URL=http://nexus-nexus.apps.ocpsno.davenet.local
export YOLODIR=/root/workspace/yolov5
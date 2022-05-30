# FROM registry.access.redhat.com/ubi8/python-38:latest for raspberry pi
# FROM ubi8/python-38:latest
# FROM model:latest
FROM ubi8/python-38:latest
USER 1001
RUN pip3 install flask requests bs4 flask_restful waitress
RUN git clone https://github.com/ultralytics/yolov5
ADD --chown=default http://pn-50.davenet.local:8081/repository/simple-artifacts/yolov5/yolov5s.pt /opt/app-root/src/yolov5/yolov5s.pt
WORKDIR yolov5
USER root
RUN pip install -r requirements.txt 

USER root
RUN yum install -y libGL
RUN pip install psutil IPython
RUN pip3 install flask requests bs4 flask_restful waitress twine
RUN pip3 install opencv-python

USER 1001
WORKDIR /opt/app-root/src
COPY flask flask
ENV FLASK_APP=flask/main.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV CAPTURE_PATH=/data/simplevis
ENV YOLODIR=/opt/app-root/src/yolov5

EXPOSE 5000
ENTRYPOINT ["/opt/app-root/src/flask/main.py"]

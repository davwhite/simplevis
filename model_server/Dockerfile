FROM ubi8/python-38:latest
# ARG UID=1000

# RUN yum -y update
RUN pip3 install flask requests bs4 flask_restful waitress
RUN git clone https://github.com/ultralytics/yolov5
WORKDIR yolov5 
RUN pip install -r requirements.txt 
USER root
RUN yum install -y libGL
RUN pip install psutil IPython

COPY flask flask
# RUN get_the_funcs.py
ENV FLASK_APP=flask/main.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV NEXUS_USER=admin
ENV NEXUS_PASS=admin123
ENV NEXUS_URL=http://nexus-nexus.apps.ocpsno.davenet.local
ENV YOLODIR=/opt/app-root/src/yolov5

EXPOSE 5000
# ENV LC_ALL=en_US.utf-8
# ENV LANG=en_US.utf-8
ENTRYPOINT ["/opt/app-root/src/flask/main.py"]

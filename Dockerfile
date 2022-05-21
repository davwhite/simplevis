FROM ubi8/python-38:latest
RUN git clone https://github.com/ultralytics/yolov5
WORKDIR yolov5 
RUN pip install -r requirements.txt 
USER root
RUN yum install -y libGL
RUN pip install psutil IPython
COPY simplevis.py simplevis.py
COPY infer.sh infer.sh
CMD /opt/app-root/src/yolov5/infer.sh

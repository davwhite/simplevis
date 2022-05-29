FROM ubi8/python-38:latest
COPY flask flask
RUN pip3 install flask requests bs4 flask_restful waitress

ENV FLASK_APP=flask/spp.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV CAPTURE_PATH=/opt/app-root/src/flask/static
ENV MODEL_SERVER="http://ocpedge:5000"

ENTRYPOINT ["/opt/app-root/src/flask/app.py"]
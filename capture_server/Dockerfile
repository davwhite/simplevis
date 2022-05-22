FROM ubi8/python-38:latest
# ARG UID=1000

# RUN yum -y update
RUN pip3 install flask requests bs4 flask_restful waitress
COPY flask flask

ENV FLASK_APP=flask/main.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV CAPTURE_PATH=/tmp
ENV NEXUS_USER=admin
ENV NEXUS_PASS=admin123

EXPOSE 5000
# ENV LC_ALL=en_US.utf-8
# ENV LANG=en_US.utf-8
ENTRYPOINT ["/opt/app-root/src/flask/main.py"]
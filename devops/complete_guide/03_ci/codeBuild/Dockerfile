FROM python:3.11.3

RUN mkdir -p /opt/my_repo
WORKDIR /opt/my_repo
RUN mkdir /my_subdir

ADD code.zip ./code.zip
RUN unzip code.zip
RUN chmod +x main.py

ENTYPOINT ["python"]

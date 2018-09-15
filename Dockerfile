FROM python:3.6
MAINTAINER MyPoZi
RUN pip install requests pandas
COPY * /python/

FROM python:3.6
MAINTAINER MyPoZi
RUN pip install requests pandas
COPY /src /home/kit/python/src

# Install sqlite3
RUN mkdir /home/kit/sqlite3 && \
    cd /home/kit/sqlite3 && \
    wget https://www.sqlite.org/2018/sqlite-autoconf-3240000.tar.gz && \
    tar vxzf sqlite-autoconf-3240000.tar.gz && \
    rm sqlite-autoconf-3240000.tar.gz && \
    cd sqlite-autoconf-3240000 && \
    ./configure && \
    make && \
    make install

FROM python:3.7
RUN mkdir -p /home/work/AutomationPlatform/automatedtest_backend
WORKDIR /home/work/AutomationPlatform/automatedtest_backend
COPY requirements.txt /home/work/AutomationPlatform/automatedtest_backend
EXPOSE 8009
#RUN apt-get update && apt-get install python3-pip -y && apt-get install mysql-client libmysqlclient-dev libssl-dev  libcrypto++-dev -y
RUN pip3 install --upgrade pip
RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple Cython
RUN pip3 install  -r requirements.txt
COPY . /home/work/AutomationPlatform/automatedtest_backend
WORKDIR /home/work/AutomationPlatform/automatedtest_backend
ENTRYPOINT uwsgi --ini uwsgi.ini
#CMD  echo "hello docker" 
#ENTRYPOINT python debug_manage.py runserver 0.0.0.0:8009
#FROM ubuntu
#RUN apt-get update && apt-get install redis-server -y
#
#docker build -t ubuntu_redis:v01
#RUN apt-get update && apt-get install python3-pip net-tools openssh-server -y

FROM python:3.5-slim

MAINTAINER Sahand Hariri sahandha@gmail.com
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*

RUN sudo apt-get install -y python-pip
RUN sudo apt-get install -y git
RUN pip install --upgrade pip
RUN pip install git+https://github.com/kubernetes-client/python.git
RUN pip install motor

Add ../server/kube_deploy.py /external/server
Add sched.py /external/server

RUN apt-get install -y vim; exit 0

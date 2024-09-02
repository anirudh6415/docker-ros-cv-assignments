FROM osrf/ros:humble-desktop-full

RUN apt-get update && apt-get install -y git wget python3-pip vim
RUN pip3 install setuptools==58.2.0

COPY ros2_ws/ /root/ros2_ws/
ENV DISPLAY=novnc:0.0

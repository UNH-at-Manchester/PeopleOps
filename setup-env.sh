#! /usr/bin/env bash

sudo yum update
sudo yum install -y python34
sudo pip install --upgrade pip
sudo yum install -y python3-pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip-py
pip3 install jupyter
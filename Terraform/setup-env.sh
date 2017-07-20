#! /usr/bin/env bash

sudo yum -y update
sudo yum install -y python34
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

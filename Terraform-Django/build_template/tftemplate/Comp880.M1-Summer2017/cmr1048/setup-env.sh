#! /usr/bin/env bash
#cmr1048's setup-env.sh File

sudo yum -y update
sudo yum install -y python34
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

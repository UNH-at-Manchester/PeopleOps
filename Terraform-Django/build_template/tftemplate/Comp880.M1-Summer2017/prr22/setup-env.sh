#! /usr/bin/env bash
#prr22's setup-env.sh File

sudo yum -y update
sudo yum install -y python34
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

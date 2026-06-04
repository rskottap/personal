#!/bin/bash

version="3.11.9"
dir="~/Desktop/repos/extra/"
cd $dir
wget https://www.python.org/ftp/python/${version}/Python-${version}.tgz
tar xzf Python-${version}.tgz
cd Python-${version}
./configure --enable-optimizations
make -j $(nproc)
sudo make altinstall


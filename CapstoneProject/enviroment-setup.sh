#!/usr/bin/env bash
#bash command to setup enviroment

#System packages
sudo apt install -y python3-venv pigpiod libjbig0 libjpeg-dev liblcms2-2 libopenjp2-7 libtiff5 libwebp6 libwebpdemux2 libwebpmux3 libzstd1 libatlas3-base libgfortran5 git tmux

# Download the BrachioGraph library
git clone https://github.com/evildmp/BrachioGraph.git

# Python packages
pip3 install -r BrachioGraph/requirements.txt


# Start it all up
sudo pigpiod
python3 -m venv env
source env/bin/activate

#
cd BrachioGraph

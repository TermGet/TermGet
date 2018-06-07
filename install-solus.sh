#!/bin/bash

pm=eopkg

echo "setting up directories"
sudo bash -c "mkdir /usr/share/termget 2> /dev/null" # create new config directory if one doesn't exist
echo "... installing program to /usr/local/bin"
chmod +x termget.py
sudo cp termget.py /usr/bin/termget # copy program to PATH

echo "... generating package file"
sudo bash -c "echo -n $pm > /usr/share/termget/termget-package-manager" # copy package file to config directory

echo -e "\nSuccessfully Installed!"

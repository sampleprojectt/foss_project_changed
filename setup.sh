#!/bin/sh
sudo add-apt-repository universe
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip # Required to install 'requests' module and install/upgrade the package 'youtube-dl'
pip3 install requests # Installs the 'requests' module used in 'main.py'
sudo pip3 install --upgrade youtube_dl # Installs/upgrades the package 'youtube-dl' that is required in 'main.py'
echo "Installation Successful. You may now run the project"
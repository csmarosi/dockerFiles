#!/bin/bash
set -euxo pipefail

cd ${HOME}
shopt -s dotglob
#/tmp and ${HOME} is bind mounted from a permanent place
sudo rm -rf /tmp/*

echo $(whoami):$(whoami) | sudo chpasswd
sudo /etc/init.d/xrdp.sh start

#test -S /tmp/.X11-unix/X0
sleep infinity

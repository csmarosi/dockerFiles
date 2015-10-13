#!/bin/bash
set -x
set -e

cmdArg="${1}"
#Note: This file heavily relies on some of my private files

#A password is needed, but on local network does not really matter what
echo $(whoami):$(whoami) | sudo chpasswd
export PATH=${PATH}:${HOME}/browser_profiles/

if [[ "${DISPLAY}" == ":0" ]]; then
    exec ${cmdArg}
else
    cd ${HOME}
    cp .ratpoisonrc.common .ratpoisonrc
    echo "exec bash -c 'PULSE_SERVER=${PULSE_SERVER} ${HOME}/browser_profiles/${cmdArg}'" >> .ratpoisonrc
    sudo /etc/init.d/xrdp.sh start
    exec sleep infinity
fi

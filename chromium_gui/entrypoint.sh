#!/bin/bash
set -x
set -e

#Note: This file heavily relies on some of my private files
cmdArg="${1}"

if [[ "${DISPLAY}" == ":0" ]]; then
    exec ${HOME}/browser_profiles/${cmdArg}
else
    #A password is needed, but on local network does not really matter what
    echo $(whoami):$(whoami) | sudo chpasswd
    cd ${HOME}
    cp .ratpoisonrc.common .ratpoisonrc
    echo "exec bash -c 'PULSE_SERVER=${PULSE_SERVER} ${HOME}/browser_profiles/${cmdArg}'" >> .ratpoisonrc
    sudo /etc/init.d/xrdp.sh start
    exec sleep infinity
fi

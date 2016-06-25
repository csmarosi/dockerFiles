#!/bin/bash
set -x
set -e

cd ${HOME}
profileGenerator=${HOME}/browser_profiles/chromiumPrivate.py
if [ -f ${profileGenerator} ]; then
    cp .ratpoisonrc.common .ratpoisonrc
else
    profileGenerator=/tmp/chromium.py
fi

cat > /tmp/start.sh <<EOF
export PULSE_SERVER=${PULSE_SERVER}
export dockerImageName=${dockerImageName}
exec ${profileGenerator}
EOF

if [[ "${DISPLAY}" == ":0" ]]; then
    exec bash /tmp/start.sh
else
    #A password is needed, but on local network does not really matter what
    echo $(whoami):$(whoami) | sudo chpasswd
    echo 'exec bash /tmp/start.sh' >> .ratpoisonrc
    sudo /etc/init.d/xrdp.sh start
    exec sleep infinity
fi

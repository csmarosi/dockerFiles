#!/bin/bash
set -x
set -e

export HOME=/tmp/home

mkdir -p ${HOME}/.config/chromium/ ${HOME}/.config/google-chrome/
touch "${HOME}/.config/chromium/First Run"
touch "${HOME}/.config/google-chrome/First Run"

if [ -f /usr/bin/google-chrome ]; then
    exec /usr/bin/google-chrome --no-sandbox
else
    exec chromium-browser --no-sandbox
fi

#!/bin/bash
set -x
set -e

profileGenerator=${HOME}/browser_profiles/chromium.py
export HOME=/tmp/home

browserConfigPath=${HOME}/.config/chromium/
exePath=/usr/bin/chromium-browser
if [ -f /usr/bin/google-chrome ]; then
    browserConfigPath=${HOME}/.config/google-chrome/
    exePath=/usr/bin/google-chrome
fi

mkdir -p ${browserConfigPath}
touch "${browserConfigPath}/First Run"

if [ -f ${profileGenerator} ]; then
    python3 ${profileGenerator}
else
    ${exePath} --no-sandbox
fi

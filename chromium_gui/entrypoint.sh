#!/bin/bash
set -x
set -e

profileGenerator=${HOME}/browser_profiles/chromiumPrivate.py
if [ ! -f ${profileGenerator} ]; then
    profileGenerator=/tmp/chromium.py
fi

exec ${profileGenerator}

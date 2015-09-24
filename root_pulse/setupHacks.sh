#!/bin/bash
set -x
set -e

amixer sset 'Master',0 100 unmute
/usr/bin/pulseaudio \
    --system \
    --daemonize=false \
    -n \
    --file=/config.pa \
    --disallow-exit \
    --disallow-module-loading

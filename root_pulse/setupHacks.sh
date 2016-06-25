#!/bin/bash
set -x
set -e

cat > /config.pa <<EOF
load-module module-alsa-sink sink_name=output device=hw:0
set-default-sink output
load-module module-native-protocol-tcp auth-ip-acl=0.0.0.0/0 auth-anonymous=1
EOF

amixer sset 'Master',0 100 unmute
exec /usr/bin/pulseaudio \
    --system \
    --daemonize=false \
    -n \
    --file=/config.pa \
    --disallow-exit \
    --disallow-module-loading

#!/bin/bash
set -euxo pipefail

card=0
if ! amixer sset 'Master',0 100 unmute; then
    card=1
    amixer --card ${card} sset 'Master',0 100 unmute
fi

cat >/config.pa <<EOF
load-module module-alsa-sink sink_name=output device=hw:${card}
set-default-sink output
load-module module-native-protocol-tcp auth-ip-acl=0.0.0.0/0 auth-anonymous=1
EOF

exec /usr/bin/pulseaudio \
    --system \
    --daemonize=false \
    -n \
    --file=/config.pa \
    --disallow-exit \
    --disallow-module-loading

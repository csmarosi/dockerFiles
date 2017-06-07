#!/bin/bash
set -x
set -e

test -f /magic2/script_to_execute.sh && bash $_ || true

configFile=/magic/${1}
test -f ${configFile}

remoteIp=$(awk '/^remote /{print $2}' ${configFile})
currentRoute=$(ip route get ${remoteIp}/32 | head -n1 | cut -d' ' -f3)
ip route | grep -q ${remoteIp} || \
    ip route add ${remoteIp} via ${currentRoute}
ip route | grep -q 192.168.0.0/16 || \
    ip route add 192.168.0.0/16 via ${currentRoute}

openvpn ${configFile} &
while ! ip addr | grep -Eq 'inet .*(tun|tap)'; do
    sleep 1
done

newRoute=$(ip route | grep -E 'tun|tap' | awk '/via/{print $3}' | head -n1)
ip route change default via ${newRoute}

exec sleep infinity

#!/bin/bash
set -x
set -e

configFile=/magic/client-config.ovpn
test -f ${configFile}

remoteIp=$(awk '/^remote/{print $2}' ${configFile})
currentRoute=$(ip route show ${remoteIp}/0 | cut -d' ' -f3)
ip route add ${remoteIp} via ${currentRoute}
ip route add 192.168.0.0/16 via ${currentRoute}

openvpn ${configFile} &
while ! ip addr | grep -Eq 'inet .*(tun|tap)'; do
    sleep 1
done

newRoute=$(ip route | grep -E 'tun|tap' | awk '/via/{print $3}' | head -n1)
ip route change default via ${newRoute}

exec sleep infinity

#!/bin/bash
set -euxo pipefail

echo -n >/etc/resolv.conf
counter=1
for dnsServer in ${@}; do
    counter=$((counter + 1))
    if ip route get ${dnsServer}; then
        echo nameserver ${dnsServer} >>/etc/resolv.conf
        continue
    fi
    listenIp="127.0.0.${counter}"
    echo nameserver ${listenIp} >>/etc/resolv.conf
    /usr/sbin/dnscrypt-proxy -Z ${dnsServer} -R ${dnsServer} -a ${listenIp}:53 &
done

cat /etc/resolv.conf
exec /usr/sbin/dnsmasq

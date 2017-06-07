#!/bin/bash
set -x
set -e

counter=1
for dnsServer in ${@}; do
    counter=$((${counter} + 1))
    listenIp="127.0.0.${counter}"
    echo nameserver ${listenIp} >> /etc/resolv.conf.all
    /usr/sbin/dnscrypt-proxy -Z ${dnsServer} -R ${dnsServer} -a ${listenIp}:53 &
done

shuf -n3 /etc/resolv.conf.all > /etc/resolv.conf
cat /etc/resolv.conf
exec /usr/sbin/dnsmasq

#!/bin/bash
set -x
set -e

cat > /etc/torrc <<EOF
VirtualAddrNetworkIPv4 10.192.0.0/10
AutomapHostsOnResolve 1
TransPort 9040
DNSPort 53
User debian-tor
DataDirectory /var/lib/tor
EOF

cat > /etc/resolv.conf <<EOF
nameserver 127.0.0.1
EOF

iptables -F
iptables -t nat -F
_tor_uid=$(awk -F: '/^debian-tor:/{print $3}' /etc/passwd)
iptables -t nat -A OUTPUT -m owner --uid-owner $_tor_uid -j RETURN
iptables -t nat -A OUTPUT -d 127.0.0.0/8 -j RETURN
iptables -t nat -A OUTPUT -d 192.168.0.0/16 -j RETURN
iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports 9040
iptables -A OUTPUT -m owner --uid-owner $_tor_uid -j ACCEPT
iptables -A OUTPUT -d 127.0.0.0/8 -j ACCEPT
iptables -A OUTPUT -d 192.168.0.0/16 -j ACCEPT
iptables -A OUTPUT -m state --state ESTABLISHED -j ACCEPT
iptables -A OUTPUT -j REJECT

/usr/sbin/tor -f /etc/torrc

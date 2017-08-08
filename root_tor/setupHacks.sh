#!/bin/bash
set -x
set -e

test -f /etc/torrc || cat > /etc/torrc <<EOF
VirtualAddrNetworkIPv4 10.192.0.0/10
AutomapHostsOnResolve 1
TransPort 9040
DNSPort 53
User debian-tor
DataDirectory /var/lib/tor
ControlSocket /tmp/tor/ctrl

TrackHostExits .
TrackHostExitsExpire 36123
EOF
socketDir=/tmp/tor
mkdir ${socketDir} && chmod 700 ${socketDir} && chown debian-tor ${socketDir}

cat > /etc/resolv.conf <<EOF
nameserver 127.0.0.1
EOF

iptables -F
iptables -P FORWARD DROP
iptables -P OUTPUT DROP
iptables -t nat -F
_tor_uid=$(awk -F: '/^debian-tor:/{print $3}' /etc/passwd)
iptables -t nat -A OUTPUT -o tun+ -j RETURN
iptables -t nat -A OUTPUT -m owner --uid-owner $_tor_uid -j RETURN
iptables -t nat -A OUTPUT -d 127.0.0.0/8 -j RETURN
iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports 9040
iptables -A OUTPUT -o tun+ -j ACCEPT
iptables -A OUTPUT -m owner --uid-owner $_tor_uid -j ACCEPT
iptables -A OUTPUT -d 127.0.0.0/8 -j ACCEPT
iptables -A OUTPUT -m state --state ESTABLISHED -j ACCEPT
iptables -A OUTPUT -j REJECT

/usr/sbin/tor -f /etc/torrc

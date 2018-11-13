#!/bin/bash
set -exo pipefail

cat >/etc/dnsmasq.conf <<EOF
user=root
port=53
address=/#/${PROXY_ADDRESS}
EOF
if [ -n "${PROXY_ADDRESS}" ]; then
    /etc/init.d/dnsmasq start
    echo nameserver 127.0.0.1 >/etc/resolv.conf
fi

#mysql_install_db --datadir=/var/lib/mysql --user=mysql
/etc/init.d/mysql start
/etc/init.d/apache2 start
/etc/init.d/tt-rss start

echo "30 3 * * * root /tt-rss/backup.sh" >/etc/cron.d/backup
/etc/init.d/cron start

sleep infinity

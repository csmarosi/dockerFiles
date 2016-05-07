#!/bin/bash
set -x
set -e

#mysql_install_db --datadir=/var/lib/mysql --user=mysql
/etc/init.d/mysql start
/etc/init.d/apache2 start
/etc/init.d/tt-rss start

echo "30 3 * * * root /tt-rss/backup.sh" > /etc/cron.d/backup
/etc/init.d/cron start

sleep infinity

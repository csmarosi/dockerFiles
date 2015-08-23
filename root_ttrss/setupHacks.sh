#!/bin/bash
set -x
set -e

#mysql_install_db --datadir=/var/lib/mysql --user=mysql
/etc/init.d/mysql start
/etc/init.d/apache2 start
/etc/init.d/tt-rss start

bash

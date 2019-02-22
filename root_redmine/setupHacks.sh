#!/bin/bash
set -euxo pipefail

/etc/init.d/mysql start
/etc/init.d/apache2 start

echo "51 13 * * * root /redmine/backup.sh" >/etc/cron.d/backup
/etc/init.d/cron start

sleep infinity

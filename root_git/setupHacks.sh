#!/bin/bash
set -euxo pipefail

/etc/init.d/ssh start

echo "3 5 * * * root /backup.sh" >/etc/cron.d/backup
/etc/init.d/cron start

#no exec to reap the zombies
sleep infinity

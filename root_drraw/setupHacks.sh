#!/bin/bash
set -euxo pipefail

/etc/init.d/apache2 start
/etc/init.d/ssh start

while true; do
    /root/collectd.sh
    sleep $((19 * 59 * 61))
done

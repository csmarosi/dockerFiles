#!/bin/bash
set -x
set -e

/etc/init.d/apache2 start
/etc/init.d/ssh start

while true; do
    /root/collectd.sh
    sleep $((19 * 59 * 61))
done

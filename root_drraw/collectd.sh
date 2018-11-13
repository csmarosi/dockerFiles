#!/bin/bash
set -x
set -e

cd /var/www/collectd/
for host in $(awk '/Host /{print $2}' ~/.ssh/config); do
    dirName=$(ssh ${host} 'ls -d /var/lib/collectd/rrd/*')
    scp -rp ${host}:${dirName} /var/www/collectd/
done

for i in /var/www/collectd/*; do
    grep $i /etc/drraw/drraw.conf ||
        sed -e "/^%datadirs/ a '$i' => '[$(basename $i)]'," -i /etc/drraw/drraw.conf
done

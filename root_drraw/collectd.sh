#!/bin/bash
set -euxo pipefail

cd /var/www/collectd/
rm -rf /var/www/collectd/*
for host in $(awk '/Host /{print $2}' ~/.ssh/config); do
    dirName=$(ssh ${host} 'ls -d /var/lib/collectd/rrd/*')
    scp -rp ${host}:${dirName} /var/www/collectd/
    rrdDir=/var/www/collectd/$(basename ${dirName})
    #WA for AVG failing for a single item: always have multiple CPUs!
    if ! test -d ${rrdDir}/cpu-1; then
        cp -R ${rrdDir}/cpu-0 ${rrdDir}/cpu-1
    fi
done

for i in /var/www/collectd/*; do
    grep $i /etc/drraw/drraw.conf ||
        sed -e "/^%datadirs/ a '$i' => '[$(basename $i)]'," -i /etc/drraw/drraw.conf
done

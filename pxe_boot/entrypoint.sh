#!/bin/bash
set -x
#no -e!

/etc/init.d/dnsmasq start
bash

/etc/init.d/dnsmasq stop
echo Done!

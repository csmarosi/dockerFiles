#!/bin/bash
set -x
set -e

/etc/init.d/ssh start

#no exec to reap the zombies
sleep infinity

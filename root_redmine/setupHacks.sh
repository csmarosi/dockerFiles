#!/bin/bash
set -x
set -e

/etc/init.d/mysql start
/etc/init.d/apache2 start

bash

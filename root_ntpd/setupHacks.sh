#!/bin/bash
set -euxo pipefail

#require `--cap-add SYS_TIME`
/etc/init.d/ntp start
sleep infinity

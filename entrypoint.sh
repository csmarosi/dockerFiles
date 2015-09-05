#!/bin/bash
set -x
set -e

cmdArg="${1}"

if echo ${cmdArg} | grep -q 'pdf$'; then
    okular /magic/$(basename ${cmdArg})
elif echo ${cmdArg} | grep -q 'callgrind'; then
    kcachegrind /magic/$(basename ${cmdArg})
elif [ -n "${1}" ]; then
    cd ${HOME}
    ${@}
else
    bash
fi

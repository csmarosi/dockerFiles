#!/bin/bash
set -x
set -e

cmdArg="${1}"
fileToOpen=/magic/$(basename ${cmdArg} || true)

if type file && file --mime-type ${fileToOpen} | \
   grep -E 'tion/.*opendoc|tion/.*openxml|tion/.*ms'; then
    libreoffice ${fileToOpen}
    exit 0
fi

if echo ${cmdArg} | grep -q 'pdf$'; then
    okular ${fileToOpen}
elif echo ${cmdArg} | grep -q 'callgrind'; then
    kcachegrind ${fileToOpen}
elif test -n "${cmdArg}" && type ${cmdArg}; then
    cd ${HOME}
    ${@}
else
    bash
fi

#!/bin/bash
set -x
set -e

buildOptions=''
if [ '--no-cache' == "${1}" ]; then
    buildOptions='--no-cache'
    shift
fi

test -n "${1}"
test -z "${2}"
imageName=${1}

sudo docker build ${buildOptions} -t ${imageName} -f ${imageName}/Dockerfile .

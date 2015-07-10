#!/bin/bash
set -x
set -e

test -n "${1}"
test -z "${2}"
imageName=${1}

sudo docker build -t ${imageName} -f ${imageName}/Dockerfile ${imageName}
